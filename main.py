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
import time  # 导入此模块，获取当前时间


def timed_start(my_hour = '11',my_minute = '35'):
    flag = 1
    while flag:
        t = time.localtime()  # 当前时间的纪元值
        fmt = "%H %M"
        now = time.strftime(fmt, t)  # 将纪元值转化为包含时、分的字符串
        now = now.split(' ') #以空格切割，将时、分放入名为now的列表中
    
        hour = now[0]
        minute = now[1]
        if hour == my_hour and minute == my_minute:
            music = 'it is time to start'
            print(music)
            flag = 0


if __name__ == '__main__':
    crawler = Crawler(just_run_once = False)
    # crawler = Crawler(just_run_once = False, freq=21600) # freq unit is second
    # crawler = Crawler(just_run_once = True)
    # timed_start("18","08")
    timed_start()
    crawler.run()
