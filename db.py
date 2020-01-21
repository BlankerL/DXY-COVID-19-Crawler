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
        self.collection = db['DXY']

    def insert(self, data):
        self.collection.insert(data)

    def find_one(self, province_name=None, modify_time=None):
        return self.collection.find_one(
            {
                'provinceName': province_name,
                'modifyTime': modify_time
            }
        )
