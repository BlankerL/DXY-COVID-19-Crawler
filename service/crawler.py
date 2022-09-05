"""
@ProjectName: DXY-2019-nCov-Crawler
@FileName: crawler.py
@Author: Jiabao Lin
@Date: 2020/1/21

@modify by peikai li
@ on Wed May 25 17:02:09 2022
"""
import sys
sys.path.append("../")

from bs4 import BeautifulSoup
from service.db import DB
from service.userAgent import user_agent_list
from service.nameMap import country_type_map, city_name_map, country_name_map, continent_name_map
import re
import json
import time
import random
import logging
import requests
import datetime


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)


class Crawler:
    def __init__(self, just_run_once = True,freq = 28800):
        self.session = requests.session()
        self.db = DB()
        self.crawl_timestamp = int()
        self.just_run_once = just_run_once
        self.freq = freq

    def run(self):
        while True:
            self.crawler()
            if self.just_run_once:
                break
            # time.sleep(120) # 120s 爬取一次
            time.sleep(self.freq) # 8h 爬取一次         

    def crawler(self):
        while True:
            self.session.headers.update(
                {
                    'user-agent': random.choice(user_agent_list)
                }
            )
            self.crawl_timestamp = int(time.time() * 1000)
            self._today = datetime.datetime.now().strftime('%m/%d/%Y')
            
            try:
                r = self.session.get(url='https://ncov.dxy.cn/ncovh5/view/pneumonia')
                r.encoding = 'utf-8'
                self.session.close()
            except requests.exceptions.ChunkedEncodingError:
                continue
            soup = BeautifulSoup(r.content, 'lxml')

            overall_information = re.search(r'(\{"id".*\})\}', str(soup.find('script', attrs={'id': 'getStatisticsService'})))
            if overall_information:
                self.overall_parser(overall_information=overall_information)

            # 国内
            area_information = re.search(r'\[(.*)\]', str(soup.find('script', attrs={'id': 'getAreaStat'})))
            if area_information:
                self.area_parser(area_information=area_information)

            area_fetchRecentStatV2 = re.search(r'\[(.*)\]', str(soup.find('script', attrs={'id': 'fetchRecentStatV2'})))
            if area_fetchRecentStatV2:
                self.area_fetch_parser(area_fetchRecentStatV2=area_fetchRecentStatV2)
    
            # 国外
            abroad_information = re.search(r'\[(.*)\]', str(soup.find('script', attrs={'id': 'getListByCountryTypeService2true'})))
            if abroad_information:
                self.abroad_parser(abroad_information=abroad_information)

            news_chinese = re.search(r'\[(.*?)\]', str(soup.find('script', attrs={'id': 'getTimelineService1'})))
            if news_chinese:
                self.news_parser(news=news_chinese)

            news_english = re.search(r'\[(.*?)\]', str(soup.find('script', attrs={'id': 'getTimelineService2'})))
            if news_english:
                self.news_parser(news=news_english)

            rumors = re.search(r'\[(.*?)\]', str(soup.find('script', attrs={'id': 'getIndexRumorList'})))
            if rumors:
                self.rumor_parser(rumors=rumors)

            if not overall_information or \
                    not area_information or \
                    not area_fetchRecentStatV2 or\
                    not abroad_information:
                    # not abroad_information or \
                    # not news_chinese or \
                    # not news_english or \
                    # not rumors:
                time.sleep(3)
                # 全都有数据才能停止，否则一直无线循环的爬
                continue

            break

        logger.info('Successfully crawled.')


    def overall_parser(self, overall_information):
          # .group(0)==group() 表示所有的re结果，.group(1)表目标为第一个
        overall_information = json.loads(overall_information.group(1))
        overall_information.pop('id')
        overall_information.pop('createTime')
        overall_information.pop('modifyTime')
        overall_information.pop('imgUrl')
        overall_information.pop('deleted')
        overall_information['countRemark'] = overall_information['countRemark'].replace(' 疑似', '，疑似').replace(' 治愈', '，治愈').replace(' 死亡', '，死亡').replace(' ', '')
        
        # 去重限定日期
        overall_information['_today'] = self._today
        if not self.db.find_one(collection='DXYOverall', data=overall_information):
            # find_one去重,如果数据库里面找到了这一条完全一样的信息，就停止爬取
            overall_information['updateTime'] = self.crawl_timestamp

            self.db.insert(collection='DXYOverall', data=overall_information)

    # def province_parser(self, province_information):
    #     provinces = json.loads(province_information.group(0))
    #     for province in provinces:
    #         province.pop('id')
    #         province.pop('tags')
    #         province.pop('sort')
    #         province['comment'] = province['comment'].replace(' ', '')

    #         if self.db.find_one(collection='DXYProvince', data=province):
    #             continue

    #         province['provinceEnglishName'] = city_name_map[province['provinceShortName']]['engName']
    #         province['crawlTime'] = self.crawl_timestamp
    #         province['country'] = country_type_map.get(province['countryType'])

    #         self.db.insert(collection='DXYProvince', data=province)


    def area_fetch_parser(self,area_fetchRecentStatV2):
        """
        无症状感染者
    
        Parameters
        ----------
        area_information : TYPE
            DESCRIPTION.
    
        Returns
        -------
        None.
    
        """
        area_information = json.loads(area_fetchRecentStatV2.group(0))
        for area in area_information:
            # 遍历所有地区
            
            # Because the cities are given other attributes,
            # this part should not be used when checking the identical document.
            
            # But I think if city information changed 
            # we still should save this difference, 
            # so I comment code about pop('cities')
            # cities_backup = area.pop('cities')
    
            # 去重限定日期
            area['_today'] = self._today
            if self.db.find_one(collection='DXYArea_f', data=area):
                continue
    
            # If this document is not in current database, insert this attribute back to the document.
            # area['cities'] = cities_backup
    
            area['countryName'] = '中国'
            area['countryEnglishName'] = 'China'
            area['continentName'] = '亚洲'
            area['continentEnglishName'] = 'Asia'
            area['provinceEnglishName'] = city_name_map[area['provinceShortName']]['engName']
    
            for city in area['cities']:
                if city['cityName'] != '待明确地区':
                    try:
                        city['cityEnglishName'] = city_name_map[area['provinceShortName']]['cities'][city['cityName']]
                    except KeyError:
                        print(area['provinceShortName'], city['cityName'])
                        pass
                else:
                    city['cityEnglishName'] = 'Area not defined'
            
            area['updateTime'] = self.crawl_timestamp
    
            self.db.insert(collection='DXYArea_f', data=area)
            
            
    def area_parser(self, area_information):
        area_information = json.loads(area_information.group(0))
        for area in area_information:
            area['comment'] = area['comment'].replace(' ', '')

            # Because the cities are given other attributes,
            # this part should not be used when checking the identical document.
            
            # But I think if city information changed 
            # we still should save this difference, 
            # so I comment code about pop('cities')
            # cities_backup = area.pop('cities')
    
            # 去重限定日期
            area['_today'] = self._today
            if self.db.find_one(collection='DXYArea_f', data=area):
                continue

            # If this document is not in current database, insert this attribute back to the document.
            # area['cities'] = cities_backup

            area['countryName'] = '中国'
            area['countryEnglishName'] = 'China'
            area['continentName'] = '亚洲'
            area['continentEnglishName'] = 'Asia'
            area['provinceEnglishName'] = city_name_map[area['provinceShortName']]['engName']

            for city in area['cities']:
                if city['cityName'] != '待明确地区':
                    try:
                        city['cityEnglishName'] = city_name_map[area['provinceShortName']]['cities'][city['cityName']]
                    except KeyError:
                        print(area['provinceShortName'], city['cityName'])
                        pass
                else:
                    city['cityEnglishName'] = 'Area not defined'

            area['updateTime'] = self.crawl_timestamp

            self.db.insert(collection='DXYArea', data=area)

    def abroad_parser(self, abroad_information):
        countries = json.loads(abroad_information.group(0))
        for country in countries:
            try:
                country.pop('id')
                country.pop('tags')
                country.pop('sort')
                # Ding Xiang Yuan have a large number of duplicates,
                # values are all the same, but the modifyTime are different.
                # I suppose the modifyTime is modification time for all documents, other than for only this document.
                # So this field will be popped out.
                country.pop('modifyTime')
                # createTime is also different even if the values are same.
                # Originally, the createTime represent the first diagnosis of the virus in this area,
                # but it seems different for abroad information.
                country.pop('createTime')
                country['comment'] = country['comment'].replace(' ', '')
            except KeyError:
                pass
            country.pop('countryType')
            country.pop('provinceId')
            country.pop('cityName')
            # The original provinceShortName are blank string
            country.pop('provinceShortName')
            # Rename the key continents to continentName
            country['continentName'] = country.pop('continents')

            # 去重限定日期
            country['_today'] = self._today
            if self.db.find_one(collection='DXYArea', data=country):
                continue

            country['countryName'] = country.get('provinceName')
            country['provinceShortName'] = country.get('provinceName')
            country['continentEnglishName'] = continent_name_map.get(country['continentName'])
            country['countryEnglishName'] = country_name_map.get(country['countryName'])
            country['provinceEnglishName'] = country_name_map.get(country['countryName'])

            country['updateTime'] = self.crawl_timestamp

            self.db.insert(collection='DXYArea', data=country)

    def news_parser(self, news):
        news = json.loads(news.group(0))
        for _news in news:
            _news.pop('pubDateStr')
            
            # 去重限定日期
            _news['_today'] = self._today
            if self.db.find_one(collection='DXYNews', data=_news):
                continue
            _news['crawlTime'] = self.crawl_timestamp

            self.db.insert(collection='DXYNews', data=_news)

    def rumor_parser(self, rumors):
        rumors = json.loads(rumors.group(0))
        for rumor in rumors:
            rumor.pop('score')
            rumor['body'] = rumor['body'].replace(' ', '')
            
            # 去重限定日期
            rumor['_today'] = self._today
            if self.db.find_one(collection='DXYRumors', data=rumor):
                continue
            rumor['crawlTime'] = self.crawl_timestamp

            self.db.insert(collection='DXYRumors', data=rumor)


if __name__ == '__main__':
    crawler = Crawler()
    crawler.run()
