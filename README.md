# 2019新型冠状病毒疫情实时爬虫

[![API Status](https://img.shields.io/website?url=https%3A%2F%2Flab.isaaclin.cn)](https://lab.isaaclin.cn/nCoV/)
[![API Usage](https://img.shields.io/badge/dynamic/json?color=orange&label=API%20Call&query=%24.count&url=https%3A%2F%2Flab.isaaclin.cn%2FnCoV%2Fapi%2Fusage)](https://lab.isaaclin.cn/nCoV/)
[![license](https://img.shields.io/github/license/BlankerL/DXY-2019-nCoV-Crawler)](https://github.com/BlankerL/DXY-2019-nCoV-Crawler/blob/master/LICENSE)

简体中文 | [English](README.en.md)

本项目为2019新型冠状病毒（2019-nCoV）疫情状况的实时爬虫，数据来源为[丁香园](https://3g.dxy.cn/newh5/view/pneumonia)。

感谢大家对本项目的支持，为了不让爬虫泛滥占用过多流量，导致其他更有需要的用户无法及时获取到丁香园的数据，请大家减少对爬虫的部署。

我已经开放了一个API接口，其他人如果需要这份数据做其他的可视化，可以直接查看并调用API来获取数据，把丁香园的流量让给更有需要的人。

API：https://lab.isaaclin.cn/nCoV/  
注：
1. **于2020年1月30日17:15开始统计API使用总人次，绝不统计单个IP的使用频率。**  
2. 为保证跨域请求能够正常进行，于2020年1月29日**切换至HTTPS协议**，若无法正常访问，请确认是否已经切换至HTTPS！

**本项目遵循MIT开源许可，同时，若引用本API，烦请在您的项目中声明引用。**


**科研人员**

近期多位高校师生与我联系，希望用这些数据做科研之用。然而，并非所有人都熟悉API的使用和JSON数据的处理，因此我部署了一个[数据仓库](https://github.com/BlankerL/DXY-2019-nCoV-Data)，直接推送大部分统计/数据分析软件可以直接打开的csv文件，希望能够减轻各位的负担。

## 初衷
衷心感谢各位医疗工作者的付出和努力，苦于没有医学背景，只能通过自己的方式，让大家增强对疫情的关注，让未感染者做好更全面的防护。

## 项目介绍
本项目每分钟访问并爬取一次数据，储存在MongoDB中，并且保存所有历史数据的更新，希望能够在未来回溯病情时能有所帮助。

爬虫本身并不复杂，可以**移步上方API，查看本爬虫能够获取到的所有信息条目**。

## 数据异常
目前发现浙江省/湖北省部分时间序列数据存在数据异常，可能的原因是丁香园数据为人工录入，某些数据可能录入错误，比如某一次爬虫获取的浙江省治愈人数为537人，数分钟后被修改回正常人数。

本项目爬虫仅从丁香园公开的数据中获取并储存数据，并不会对异常值进行判断和处理，因此如果将本数据用作科研目的，请自己对数据进行清洗。同时，我已经在Issue中开放了[异常数据反馈通道](https://github.com/BlankerL/DXY-2019-nCoV-Crawler/issues/34)，可以直接在此问题中反馈潜在的异常数据，我会定期检查并处理。

## Reference
1. 如果您仅希望通过本API在网页端实现实时数据可视化，可以参考[shfshanyue/2019-ncov](https://github.com/shfshanyue/2019-ncov)项目。该项目能够在网页后端每隔30分钟自动运行爬虫，获取最新数据，并渲染在前端直接返回，不会受到API数据返回速度的影响。
2. 如果您希望使用R语言对数据进行分析，可以参考[pzhaonet/ncovr](https://github.com/pzhaonet/ncovr)项目，该项目整合通过GitHub数据仓库/API数据提取两种模式。

## Demo
1. [pzhaonet/ncov](https://github.com/pzhaonet/ncov)  
   网站：https://ncov2020.org
2. [cuihuan/2020_wuhan](https://github.com/cuihuan/2020_wuhan)  
   可视化效果：http://cuihuan.net/wuhan/news.html
3. [hack-fang/nCov](https://github.com/hack-fang/nCov)  
   可视化效果：http://yiqing.ahusmart.com/
4. [Moyck/2019NCOV](https://github.com/Moyck/2019NCOV)

## 捐赠
本项目不需要任何捐赠。

全国各地的医疗资源都处于短缺的状态。如果希望捐赠的人，请移步各个红十字会或者官方认可的捐赠平台，他们能够更加妥善地运用这笔资金，帮助更有需要的人。

**祝大家一切都好。**
