# -*- coding: utf-8 -*-
"""
@ProjectName: DXY-2019-nCoV-Crawler
@FileName: main.py
@Author: Jiabao Lin
@Date: 2020/1/27

@modify by peikai
@ on Wed May 25 17:02:09 2022
"""
from service.crawler import Crawler


if __name__ == '__main__':
    crawler = Crawler(just_run_once = False)
    crawler.run()
