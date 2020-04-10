# COVID-19/2019-nCoV Infection Data Realtime Crawler

[![API Status](https://img.shields.io/website?url=https%3A%2F%2Flab.isaaclin.cn)](https://lab.isaaclin.cn/nCoV/)
[![API Call](https://img.shields.io/badge/dynamic/json?color=orange&label=API%20Call&query=%24.count&url=https%3A%2F%2Flab.isaaclin.cn%2FnCoV%2Fapi%2Fusage)](https://lab.isaaclin.cn/nCoV/)
[![license](https://img.shields.io/github/license/BlankerL/DXY-COVID-19-Crawler)](https://github.com/BlankerL/DXY-COVID-19-Crawler/blob/master/LICENSE)

[简体中文](README.md) | English

COVID-19/2019-nCoV infection data realtime crawler, 
the data source is [Ding Xiang Yuan](https://3g.dxy.cn/newh5/view/pneumonia).

Please reduce the deployment of crawlers in order to prevent the crawlers 
from flooding the DXY and occupying too much traffic, 
such that other users in need cannot get the data in time. 

I prepared an API for you to make visualizations and analysis, 
which is for free and does not have any limitation in using. 

API：https://lab.isaaclin.cn/nCoV  
Remarks:  
1. **The API will return both Chinese and English version of city names.**
For more information, please refer to [Issue #61](https://github.com/BlankerL/DXY-COVID-19-Crawler/issues/61).
2. **Due to the limitation of the server's bandwidth, starting from March 19, 2020, 
`/nCoV/api/overall` and `/nCoV/api/area` do not response time-series data.
You can fetch time-series data in [json](https://github.com/BlankerL/DXY-COVID-19-Data/tree/master/json) folder of the data warehouse.
If you call the API with `latest=0`, please modify the request parameters, 
otherwise, you do not need to do any modification.**

**This project is subject to the MIT open source license. 
If you use the API, please declare the reference in your project.**

**Researchers**  
Recently, many college teachers and students contacted me, 
hoping to use these data for scientific research. 
However, not everyone is familiar with the use of APIs and the format of JSON, 
so I deployed a [data warehouse](https://github.com/BlankerL/DXY-COVID-19-Data) 
to publish the latest data in CSV format, which can be easily processed and loaded by most software.

## Description
The deployed crawler will crawls the data every minutes, 
stores them into MongoDB, and saves all historical data updates. 
I hope it can be helpful in the future when backtracking the disease.

The description of the attributes is listed in the [API page](https://lab.isaaclin.cn/nCoV/).  

## Noise Data
At present, some time series data in Zhejiang and Hubei are found containing noises. 
The possible reason is the manually processed data were recorded by mistake. 

The crawler just crawl what it sees, do not deal with any noise data. 
Therefore, if you use the data for scientific research, please preprocess and clean the data properly. 

In the meantime, I opened an [issue](https://github.com/BlankerL/DXY-COVID-19-Crawler/issues/34) 
for you to report the potential noise data. I will check and remove them periodically. 

## Reference
1. If you would like to analyze the data with [R](https://www.r-project.org/),
you can refer to [pzhaonet/ncovr](https://github.com/pzhaonet/ncovr).
This project will help you to directly load data into R from either GitHub Data Warehouse or API. 

## Research
All scientific research results are for reference only.
1. [yijunwang0805/YijunWang](https://github.com/yijunwang0805/YijunWang)

## Demonstration
1. Website: https://ncov.deepeye.tech/  
   Time-series data visualization.
2. [pzhaonet/ncov](https://github.com/pzhaonet/ncov)  
   Website: https://ncov2020.org
3. [cuihuan/2020_wuhan](https://github.com/cuihuan/2020_wuhan)  
   Visualization: http://cuihuan.net/wuhan/news.html
4. [hack-fang/nCov](https://github.com/hack-fang/nCov)  
   Visualization: http://yiqing.ahusmart.com/
5. [ohdarling/2019-nCoV-Charts](https://github.com/ohdarling/2019-nCoV-Charts)  
   Visualization: https://2019-ncov-trends.tk/
6. [quadpixels/quadpixels.github.io](https://github.com/quadpixels/quadpixels.github.io)  
   Visualization: https://quadpixels.github.io/
7. [lzxue/yiqingditu](https://github.com/lzxue/yiqingditu)  
   Visualization: https://lzxue.github.io/yiqingditu/
8. [covid19viz/covid19viz.github.io](https://github.com/covid19viz/covid19viz.github.io)  
   Visualization: https://covid19viz.github.io/
9. [biluochun/data-ncov](https://github.com/biluochun/data-ncov)  
   Visualization: https://biluochun.github.io/data-ncov/index.html
10. [Moyck/2019NCOV](https://github.com/Moyck/2019NCOV)
11. [Mistletoer/NCP-historical-data-visualization-2019-nCoV-](https://github.com/Mistletoer/NCP-historical-data-visualization-2019-nCoV-)

## Donation
No donation is needed. 

Medical resources are in short supply throughout mainland China. 
If you want to donate, please move to Red Cross or officially recognized donation platforms, 
they can make better use of the funds or supplies to help those in need.

**Wish you all the best.**
