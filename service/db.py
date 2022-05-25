"""
@ProjectName: DXY-2019-nCov-Crawler
@FileName: db.py
@Author: Jiabao Lin
@Date: 2020/1/21
"""
from pymongo import MongoClient


uri = '**Confidential**'
uri = 'localhost:27017'
client = MongoClient(uri)  
db = client['2019-nCoV'] # use 2019-nCoV 有就切换，没有就创建该数据库


class DB:
    def __init__(self):
        self.db = db

    def insert(self, collection, data):
        if type(data) == dict:
            data = [data]
        self.db[collection].insert_many(data)

    def find_one(self, collection, data=None):
        return self.db[collection].find_one(data)
