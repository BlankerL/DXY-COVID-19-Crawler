# 2019新型冠状病毒疫情实时爬虫

[![API Status](https://img.shields.io/website?url=https%3A%2F%2Flab.isaaclin.cn)](https://lab.isaaclin.cn/nCoV/)
[![API Usage](https://img.shields.io/badge/dynamic/json?color=orange&label=API%20Usage&query=%24.count&url=https%3A%2F%2Flab.isaaclin.cn%2FnCoV%2Fapi%2Fusage)](https://lab.isaaclin.cn/nCoV/)
[![license](https://img.shields.io/github/license/BlankerL/DXY-2019-nCoV-Crawler)](https://github.com/BlankerL/DXY-2019-nCoV-Crawler/blob/master/LICENSE)

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

爬虫本身并不复杂，可以**移步上方API，查看本爬虫能够获取到的所有信息条目**。同时，为了减少请求频率，已经在一次请求的时候获取足够的信息，这样能把流量让给更有需要的人。

## Demo
1. [cuihuan/2020_wuhan](https://github.com/cuihuan/2020_wuhan)  
   可视化效果：http://cuihuan.net/wuhan/news.html
2. [hack-fang/nCov](https://github.com/hack-fang/nCov)  
   可视化效果：http://yiqing.ahusmart.com/
3. [Moyck/2019NCOV](https://github.com/Moyck/2019NCOV)

## 捐赠
本项目不需要任何捐赠。

全国各地的医疗资源都处于短缺的状态。如果希望捐赠的人，请移步各个红十字会或者官方认可的捐赠平台，他们能够更加妥善地运用这笔资金，帮助更有需要的人。

**祝大家一切都好。**
