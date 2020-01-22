"""
@ProjectName: DXY-2019-nCov-Crawler
@FileName: crawler.py
@Author: Jiabao Lin
@Date: 2020/1/21
"""
from bs4 import BeautifulSoup
from db import DB
from countryTypeMap import country_type
import re
import json
import time
import logging
import datetime
import requests


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
}


class Crawler:
    def __init__(self):
        self.session = requests.session()
        self.session.headers.update(headers)
        self.db = DB()
        self.crawl_timestamp = int()
        self.url = "https://3g.dxy.cn/newh5/view/pneumonia"

    def run(self):
        while True:
            self.crawler()
            time.sleep(60)

    def crawler(self):
        while True:
            self.crawl_timestamp = int(datetime.datetime.timestamp(datetime.datetime.now()) * 1000)
            r = self.session.get(url=self.url)
            soup = BeautifulSoup(r.content, 'lxml')
            province_information = re.search(r'\[(.*?)\]', str(soup.find('script', attrs={'id': 'getListByCountryTypeService1'})))
            news = re.search(r'\[(.*?)\]', str(soup.find('script', attrs={'id': 'getTimelineService'})))
            if not province_information or not news:
                continue
            self.num_parser(province_information=province_information)
            self.news_crawler(news=news)
            break

        logger.info('Successfully crawled.')

    def num_parser(self, province_information):
        provinces = json.loads(province_information.group(0))
        for province in provinces:
            if self.db.find_one(collection='DXYNumber', province_name=province['provinceName'], modify_time=province['modifyTime']):
                continue
            province.pop('id')
            province['crawlTime'] = self.crawl_timestamp
            province['country'] = country_type.get(province['countryType'])

            province['tags'] = province['tags'].replace(' ', '')

            # Parse the content with regex
            confirmed = re.search(r'确诊(.*?)例', province['tags'])
            if confirmed:
                province['confirmed'] = confirmed.group(1)
            else:
                province['confirmed'] = 0

            suspect = re.search(r'疑似(.*?)例', province['tags'])
            if suspect:
                province['suspect'] = suspect.group(1)
            else:
                province['suspect'] = 0

            cured = re.search(r'治愈(.*?)例', province['tags'])
            if cured:
                province['cured'] = cured.group(1)
            else:
                province['cured'] = 0

            death = re.search(r'死亡(.*?)例', province['tags'])
            if death:
                province['death'] = death.group(1)
            else:
                province['death'] = 0

            self.db.insert(collection='DXYNumber', data=province)

    def news_crawler(self, news):
        news = json.loads(news.group(0))
        for _news in news:
            if self.db.find_one(collection='DXYNews', summary=_news['summary'], modify_time=_news['modifyTime']):
                continue
            _news.pop('pubDateStr')
            _news['crawlTime'] = self.crawl_timestamp
            self.db.insert(collection='DXYNews', data=_news)


if __name__ == '__main__':
    crawler = Crawler()
    crawler.run()
