"""
@ProjectName: DXY-2019-nCov-Crawler
@FileName: crawler.py
@Author: Jiabao Lin
@Date: 2020/1/21
@Contributors: WH-2099,
"""
from bs4 import BeautifulSoup
from service.db import DB
from service.userAgent import user_agent_list
from service.nameMap import country_type_map, city_name_map, country_name_map, continent_name_map
import re
import json
import time
import datetime
import random
import logging
import requests


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)


class Crawler:
    def __init__(self):
        self.session = requests.sessions.Session()
        self.db = DB()
        self.crawl_timestamp = int()
        self.recordAMAPTime = datetime.datetime()

    def run(self):
        while True:
            self.crawler()
            time.sleep(60)

    def crawler(self):
        while True:
            self.session.headers.update({
                    'user-agent': random.choice(user_agent_list)
                })
            self.session
            self.crawl_timestamp = int(time.time() * 1000)
            try:
                rDXY = self.session.get(url='https://ncov.dxy.cn/ncovh5/view/pneumonia')
            except requests.exceptions.ChunkedEncodingError:
                continue
            finally:
                rDXY.close()
            soup = BeautifulSoup(rDXY.text, 'lxml')

            #update data from AMAP every 30minutes(1800s)
            if (self.recordAMAPTime - datetime.datetime.now()).seconds >= 1800:
                AMAPurl = 'http://wb.amap.com/channel.php?aoscommon=1&callback=_aosJsonpRequest1&urlname=https%3A%2F%2Fm5.amap.com%2Fws%2Fshield%2Fsearch%2Fyiqing&param=%5B%7B%22user_loc%22%3A%22%22%2C%22sign%22%3A1%7D%2C%7B%22fromchannel%22%3A%22gaode%22%2C%22version%22%3A4%2C%22first_request%22%3A1%2C%22sign%22%3A0%7D%5D&method=get'
                with self.session.get(AMAPurl) as rAMAP: 
                    rawStr = rAMAP.text
                    jsonBegin = rawStr.find('{')
                    jsonEnd = rawStr.rfind('}') + 1
                    rawJson = rawStr[jsonBegin:jsonEnd]
                    rawData = json.loads(rawJson)
                    data = rawData['data']
                    city_parser(data['citylist'])
                    pois_parser(data['pois']['one']['poilist'] + \
                                data['pois']['seven']['poilist'] + \
                                data['pois']['fourteen']['poilist'] + \
                                data['pois']['other']['poilist'])
                    self.recordAMAPTime = datetime.datetime.now()
            

            overall_information = re.search(r'(\{"id".*\}\})\}', str(soup.find('script', attrs={'id': 'getStatisticsService'})))
            if overall_information:
                self.overall_parser(overall_information=overall_information)

            area_information = re.search(r'\[(.*)\]', str(soup.find('script', attrs={'id': 'getAreaStat'})))
            if area_information:
                self.area_parser(area_information=area_information)

            abroad_information = re.search(r'\[(.*)\]', str(soup.find('script', attrs={'id': 'getListByCountryTypeService2true'})))
            if abroad_information:
                self.abroad_parser(abroad_information=abroad_information)

            news_chinese = re.search(r'\[(.*?)\]', str(soup.find('script', attrs={'id': 'getTimelineServiceundefined'})))
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
                    not abroad_information or \
                    not news_chinese or \
                    not news_english or \
                    not rumors:
                time.sleep(3)
                continue

            break

        logger.info('Successfully crawled.')

    def overall_parser(self, overall_information):
        overall_information = json.loads(overall_information.group(1))
        overall_information.pop('id')
        overall_information.pop('createTime')
        overall_information.pop('modifyTime')
        overall_information.pop('imgUrl')
        overall_information.pop('deleted')
        overall_information['countRemark'] = overall_information['countRemark'].replace(' 疑似', '，疑似').replace(' 治愈', '，治愈').replace(' 死亡', '，死亡').replace(' ', '')

        if not self.db.find_one(collection='DXYOverall', data=overall_information):
            overall_information['updateTime'] = self.crawl_timestamp

            self.db.insert(collection='DXYOverall', data=overall_information)

    def province_parser(self, province_information):
        provinces = json.loads(province_information.group(0))
        for province in provinces:
            province.pop('id')
            province.pop('tags')
            province.pop('sort')
            province['comment'] = province['comment'].replace(' ', '')

            if self.db.find_one(collection='DXYProvince', data=province):
                continue

            province['provinceEnglishName'] = city_name_map[province['provinceShortName']]['engName']
            province['crawlTime'] = self.crawl_timestamp
            province['country'] = country_type_map.get(province['countryType'])

            self.db.insert(collection='DXYProvince', data=province)

    def area_parser(self, area_information):
        area_information = json.loads(area_information.group(0))
        for area in area_information:
            area['comment'] = area['comment'].replace(' ', '')

            # Because the cities are given other attributes,
            # this part should not be used when checking the identical document.
            cities_backup = area.pop('cities')

            if self.db.find_one(collection='DXYArea', data=area):
                continue

            # If this document is not in current database, insert this attribute back to the document.
            area['cities'] = cities_backup

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
            if self.db.find_one(collection='DXYNews', data=_news):
                continue
            _news['crawlTime'] = self.crawl_timestamp

            self.db.insert(collection='DXYNews', data=_news)

    def rumor_parser(self, rumors):
        rumors = json.loads(rumors.group(0))
        for rumor in rumors:
            rumor.pop('score')
            rumor['body'] = rumor['body'].replace(' ', '')
            if self.db.find_one(collection='DXYRumors', data=rumor):
                continue
            rumor['crawlTime'] = self.crawl_timestamp

            self.db.insert(collection='DXYRumors', data=rumor)



    ### AMAP Parser
    ###  considering that a lot of data is useless
    ###  only select some
    def city_parser(self, rawList):
        for province in rawList:
            cityInfo = {}
            cityInfo['provinceName'] = province.get('name', None)
            cityInfo['provinceId'] = province.get('id', None)
            cityInfo['provinceTotal'] = province.get('total', None)
            for city in province['list']:
                cityInfo['cityName'] = city.get('name', None)
                cityInfo['cityId'] = city.get('id', None)
                cityInfo['cityLon'] = city.get('lon', None)
                cityInfo['cityLat'] = city.get('lat', None)
                cityInfo['cityLevel'] = city.get('level', None)
                cityInfo['cityCount'] = city.get('count', None)
                self.db.insert(collection='AMAPcity', data=cityInfo)

    def pois_parser(self, rawList):
        for poi in rawList:
            poisInfo = {}
            poisInfo['poiname'] = poi.get('poiname', None)
            poisInfo['lat'] = poi.get('lat', None)
            poisInfo['lon'] = poi.get('lon', None)
            poisInfo['tag'] = poi.get('tag_display_std', None)
            poisInfo['source'] = poi.get('source', None)
            self.db.insert(collection='AMAPpois', data=poisInfo)


if __name__ == '__main__':
    crawler = Crawler()
    crawler.run()
