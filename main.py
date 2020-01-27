"""
@ProjectName: DXY-2019-nCoV-Crawler
@FileName: main.py
@Author: Jiabao Lin
@Date: 2020/1/27
"""
from service.crawler import Crawler


if __name__ == '__main__':
    crawler = Crawler()
    crawler.run()
