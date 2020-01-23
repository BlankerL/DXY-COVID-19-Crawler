"""
@ProjectName: DXY-2019-nCov-Crawler
@FileName: db.py
@Author: Jiabao Lin
@Date: 2020/1/21
"""
from pymongo import MongoClient

client = MongoClient('**Confidential**')
db = client['2019-nCov']


class DB:
    def __init__(self):
        self.db = db

    def insert(self, collection, data):
        self.db[collection].insert(data)

    def find_one(self, collection, data=None, province_name=None, summary=None, modify_time=None):
        if collection == 'DXYNumber':
            return self.db[collection].find_one(
                {
                    'provinceName': province_name,
                    'modifyTime': modify_time
                }
            )
        if collection == 'DXYNews':
            return self.db[collection].find_one(
                {
                    'summary': summary,
                    'modifyTime': modify_time
                }
            )
        if collection == 'DXYArea':
            return self.db[collection].find_one(data)
