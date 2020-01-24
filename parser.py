"""
@ProjectName: DXY-2019-nCoV-Crawler
@FileName: parser.py
@Author: Jiabao Lin
@Date: 2020/1/24
"""
import re


def regex_parser(content, key):
    # Parse the content with regex
    confirmed = re.search(r'确诊(.*?)例', content[key])
    if confirmed:
        content['confirmed'] = confirmed.group(1)
    else:
        content['confirmed'] = 0

    suspect = re.search(r'疑似(.*?)例', content[key])
    if suspect:
        content['suspect'] = suspect.group(1)
    else:
        content['suspect'] = 0

    cured = re.search(r'治愈(.*?)例', content[key])
    if cured:
        content['cured'] = cured.group(1)
    else:
        content['cured'] = 0

    death = re.search(r'死亡(.*?)例', content[key])
    if death:
        content['death'] = death.group(1)
    else:
        content['death'] = 0

    return content