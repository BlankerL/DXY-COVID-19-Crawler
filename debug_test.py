# -*- coding: utf-8 -*-
"""
Created on Thu May 26 11:49:44 2022

@author: Peikai_Li
"""

from bs4 import BeautifulSoup
import re
import json
import requests
from service.nameMap import city_name_map  #, country_type_map, country_name_map, continent_name_map

# def area_fetch_parser(self,area_fetchRecentStatV2):
#         """
#         无症状感染者
    
#         Parameters
#         ----------
#         area_information : TYPE
#             DESCRIPTION.
    
#         Returns
#         -------
#         None.
    
#         """


session = requests.session()
r = session.get(url='https://ncov.dxy.cn/ncovh5/view/pneumonia')
r.encoding = 'utf-8'
soup = BeautifulSoup(r.content, 'lxml')
area_fetchRecentStatV2 = re.search(r'\[(.*)\]', str(soup.find('script', attrs={'id': 'fetchRecentStatV2'})))
# if area_fetchRecentStatV2:
#     self.area_fetch_parser(area_fetchRecentStatV2=area_fetchRecentStatV2)
    


area_information = re.search(r'\[(.*)\]', str(soup.find('script', attrs={'id': 'getAreaStat'})))
area_information = json.loads(area_information.group(0))
 
# # def area_fetch_parser(self,area_fetchRecentStatV2):
# area_information = json.loads(area_fetchRecentStatV2.group(0))
area = area_information[10]

# for area in area_information:
#     # 遍历所有地区
    
#     # Because the cities are given other attributes,
#     # this part should not be used when checking the identical document.
# cities_backup = area.pop('cities')
print(area)
print(type(area))
#     # if self.db.find_one(collection='DXYArea_f', data=area):
#     #     continue

#     # If this document is not in current database, insert this attribute back to the document.
#     area['cities'] = cities_backup

#     area['countryName'] = '中国'
#     area['countryEnglishName'] = 'China'
#     area['continentName'] = '亚洲'
#     area['continentEnglishName'] = 'Asia'
#     area['provinceEnglishName'] = city_name_map[area['provinceShortName']]['engName']

#     for city in area['cities']:
#         if city['cityName'] != '待明确地区':
#             try:
#                 city['cityEnglishName'] = city_name_map[area['provinceShortName']]['cities'][city['cityName']]
#             except KeyError:
#                 print(area['provinceShortName'], city['cityName'])
#                 pass
#         else:
#             city['cityEnglishName'] = 'Area not defined'

#     # area['updateTime'] = self.crawl_timestamp

#     # self.db.insert(collection='DXYArea_f', data=area)
    


# with open("test_record1.json","w") as f:
#     json.dump(abroad_information,f)