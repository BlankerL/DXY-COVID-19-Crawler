"""
@ProjectName: DXY-2019-nCov-Crawler
@FileName: countryTypeMap.py
@Author: Jiabao Lin
@Date: 2020/1/22
"""
country_type_map = {
    1: '中国'
}
city_name_map = {
    '黑龙江': {
        'engName': 'Heilongjiang',
        'cities': {
            '七台河': 'Qitaihe',
            '伊春': 'Yichun',
            '佳木斯': 'Jiamusi',
            '双鸭山': 'Shuangyashan',
            '哈尔滨': 'Harbin',
            '大兴安岭': 'Daxinganling',
            '大庆': 'Daqing',
            '牡丹江': 'Mudanjiang',
            '绥化': 'Suihua',
            '鸡西': 'Jixi',
            '鹤岗': 'Hegang',
            '黑河': 'Heihe',
            '齐齐哈尔': 'Qiqihar'
        }
    },
    '海南': {
        'engName': 'Hainan',
        'cities': {
            '三亚': 'Sanya',
            '儋州': 'Danzhou',
            '海口': 'Haikou',
            '万宁': 'Wanning',
            '澄迈': 'Chengmai County',
            '昌江': 'Changjiang Li Autonomous County',
            '琼海': 'Qionghai',
            '陵水': 'Lingshui Li Autonomous County',
            '临高': 'Lingao County',
            '保亭': 'Baoting Li and Miao Autonomous County',
            '文昌': 'Wenchang',
            '东方': 'Dongfang',
            '乐东': 'Ledong Li Autonomous County',
            '定安': "Ding'an County",
            '琼中': 'Qiongzhong Li and Miao Autonomous County'
        }
    },
    '福建': {
        'engName': 'Fujian',
        'cities': {
            '三明': 'Sanming',
            '南平': 'Nanping',
            '厦门': 'Xiamen',
            '宁德': 'Ningde',
            '泉州': 'Quanzhou',
            '漳州': 'Zhangzhou',
            '福州': 'Fuzhou',
            '莆田': 'Putian',
            '龙岩': 'Longyan'
        }
    },
    '河南': {
        'engName': 'Henan',
        'cities': {
            '三门峡': 'Sanmenxia',
            '信阳': 'Xinyang',
            '南阳': 'Nanyang',
            '周口': 'Zhoukou',
            '商丘': 'Shangqiu',
            '安阳': 'Anyang',
            '平顶山': 'Pingdingshan',
            '开封': 'Kaifeng',
            '新乡': 'Xinxiang',
            '洛阳': 'Luoyang',
            '漯河': 'Luohe',
            '濮阳': 'Puyang',
            '焦作': 'Jiaozuo',
            '许昌': 'Xuchang',
            '郑州': 'Zhengzhou',
            '驻马店': 'Zhumadian',
            '鹤壁': 'Hebi',
            '济源': 'Jiyuan'
        }
    },
    '上海': {
        'engName': 'Shanghai',
        'cities': {
            '上海': 'Shanghai',
            '外地来沪人员': 'People from other cities',
            '浦东新区': 'Pudong District',
            '宝山区': 'Baoshan District',
            '徐汇区': 'Xuhui District',
            '闵行区': 'Minhang District',
            '松江区': 'Songjiang District',
            '静安区': "Jing'an District",
            '长宁区': 'Changning District',
            '普陀区': 'Putuo District',
            '杨浦区': 'Yangpu District',
            '嘉定区': 'Jiading District',
            '奉贤区': 'Fengxian District',
            '虹口区': 'Hongkou District',
            '黄浦区': 'Huangpu District',
            '崇明区': 'Chongming District',
            '青浦区': 'Qingpu District',
            '金山区': 'Jinshan District'
        }
    },
    '江西': {
        'engName': 'Jiangxi',
        'cities': {
            '上饶': 'Shangrao',
            '九江': 'Jiujiang',
            '南昌': 'Nanchang',
            '吉安': "Ji'an",
            '宜春': 'Yichun',
            '抚州': 'Fuzhou',
            '新余': 'Xinyu',
            '景德镇': 'Jingdezhen',
            '萍乡': 'Pingxiang',
            '赣州': 'Ganzhou',
            '鹰潭': 'Yingtan',
            '赣江新区': 'Ganjiang New District'
        }
    },
    '广东': {
        'engName': 'Guangdong',
        'cities': {
            '东莞': 'Dongguan',
            '中山': 'Zhongshan',
            '云浮': 'Yunfu',
            '佛山': 'Foshan',
            '广州': 'Guangzhou',
            '惠州': 'Huizhou',
            '揭阳': 'Jieyang',
            '梅州': 'Meizhou',
            '汕头': 'Shantou',
            '汕尾': 'Shanwei',
            '江门': 'Jiangmen',
            '河源': 'Heyuan',
            '深圳': 'Shenzhen',
            '清远': 'Qingyuan',
            '湛江': 'Zhanjiang',
            '潮州': 'Chaozhou',
            '珠海': 'Zhuhai',
            '肇庆': 'Zhaoqing',
            '茂名': 'Maoming',
            '阳江': 'Yangjiang',
            '韶关': 'Shaoguan'
        }
    },
    '山东': {
        'engName': 'Shandong',
        'cities': {
            '东营': 'Dongying',
            '临沂': 'Linyi',
            '威海': 'Weihai',
            '德州': 'Dezhou',
            '日照': 'Rizhao',
            '枣庄': 'Zaozhuang',
            '泰安': "Tai'an",
            '济南': 'Jinan',
            '济宁': 'Jining',
            '淄博': 'Zibo',
            '滨州': 'Binzhou',
            '潍坊': 'Weifang',
            '烟台': 'Yantai',
            '聊城': 'Liaocheng',
            '莱芜': 'Laiwu',
            '菏泽': 'Heze',
            '青岛': 'Qingdao'
        }
    },
    '宁夏': {
        'engName': 'Ningxia',
        'cities': {
            '中卫': 'Zhongwei',
            '吴忠': 'Wuzhong',
            '固原': 'Guyuan',
            '石嘴山': 'Shizuishan',
            '银川': 'Yinchuan',
            '宁东': 'Ningdong County'
        }
    },
    '山西': {
        'engName': 'Shanxi',
        'cities': {
            '临汾': 'Linfen',
            '吕梁': 'Lüliang',
            '大同': 'Datong',
            '太原': 'Taiyuan',
            '忻州': 'Xinzhou',
            '晋中': 'Jinzhong',
            '晋城': 'Jincheng',
            '朔州': 'Shuozhou',
            '运城': 'Yuncheng',
            '长治': 'Changzhi',
            '阳泉': 'Yangquan'
        }
    },
    '云南': {
        'engName': 'Yunnan',
        'cities': {
            '临沧': 'Lincang',
            '丽江': 'Lijiang',
            '保山': 'Baoshan',
            '大理州': 'Dali',
            '德宏州': 'Dehong',
            '怒江': 'Nujiang',
            '文山州': 'Wenshan',
            '昆明': 'Kunming',
            '昭通': 'Zhaotong',
            '普洱': "Pu'er",
            '曲靖': 'Qujing',
            '楚雄州': 'Chuxiong',
            '玉溪': 'Yuxi',
            '红河州': 'Honghe',
            '西双版纳': 'Xishuangbanna',
            '迪庆': 'Diqing'
        }
    },
    '辽宁': {
        'engName': 'Liaoning',
        'cities': {
            '丹东': 'Dandong',
            '大连': 'Dalian',
            '抚顺': 'Fushun',
            '朝阳': 'Chaoyang',
            '本溪': 'Benxi',
            '沈阳': 'Shenyang',
            '盘锦': 'Panjin',
            '营口': 'Yingkou',
            '葫芦岛': 'Huludao',
            '辽阳': 'Liaoyang',
            '铁岭': 'Tieling',
            '锦州': 'Jinzhou',
            '阜新': 'Fuxin',
            '鞍山': 'Anshan'
        }
    },
    '浙江': {
        'engName': 'Zhejiang',
        'cities': {
            '丽水': 'Lishui',
            '台州': 'Taizhou',
            '嘉兴': 'Jiaxing',
            '宁波': 'Ningbo',
            '杭州': 'Hangzhou',
            '温州': 'Wenzhou',
            '湖州': 'Huzhou',
            '绍兴': 'Shaoxing',
            '舟山': 'Zhoushan',
            '衢州': 'Quzhou',
            '金华': 'Jinhua'
        }
    },
    '内蒙古': {
        'engName': 'Neimenggu',
        'cities': {
            '乌兰察布': 'Ulanqab',
            '乌海市': 'Wuhai',
            '兴安盟': 'Xinganmeng',
            '包头': 'Baotou',
            '呼伦贝尔': 'Hulunbuir',
            '呼和浩特': 'Hohhot',
            '巴彦淖尔': 'Bayannur',
            '赤峰': 'Chifeng',
            '通辽': 'Tongliao',
            '鄂尔多斯': 'Ordos',
            '锡林郭勒盟': 'Linguolexi',
            '阿拉善盟': 'Alashanmeng'
        }
    },
    '新疆': {
        'engName': 'Xinjiang',
        'cities': {
            '乌鲁木齐': 'Urumqi',
            '伊犁州': 'Yili',
            '克孜勒苏柯尔克孜': 'Kezilesukeerkezi',
            '克拉玛依': 'Karamay',
            '博尔塔拉': 'Boertala',
            '吐鲁番市': 'Turpan',
            '和田': 'Hetian',
            '哈密': 'Hami',
            '喀什': 'Kashen',
            '塔城': 'Tacheng',
            '巴州': 'Bayingolin Mongol Autonomous Prefecture',
            '昌吉州': 'Changji',
            '阿克苏地区': 'Akesu',
            '阿勒泰': 'Aletai',
            '兵团第四师': 'Xinjiang Production and Construction Corps 4th Division',
            '兵团第九师': 'Xinjiang Production and Construction Corps 9th Division',
            '兵团第八师石河子市': 'Shihezi, Xinjiang Production and Construction Corps 8th Division',
            '兵团第六师五家渠市': 'Wujiaqu, Xinjiang Production and Construction Corps 5th Division',
            '兵团第十二师': 'Xinjiang Production and Construction Corps 12th Division',
            '兵团第七师': 'Xinjiang Production and Construction Corps 7th Division',
        }
    },
    '四川': {
        'engName': 'Sichuan',
        'cities': {
            '乐山': 'Leshan',
            '内江': 'Neijiang',
            '凉山': 'Liangshan',
            '南充': 'Nanchong',
            '宜宾': 'Yibin',
            '巴中': 'Bazhong',
            '广元': 'Guangyuan',
            '广安': "Guang'an",
            '德阳': 'Deyang',
            '成都': 'Chengdu',
            '攀枝花': 'Panzhihua',
            '泸州': 'Luzhou',
            '甘孜': 'Ganzi',
            '眉山': 'Meishan',
            '绵阳': 'Mianyang',
            '自贡': 'Zigong',
            '资阳': 'Ziyang',
            '达州': 'Dazhou',
            '遂宁': 'Suining',
            '阿坝': 'Aba',
            '雅安': "Ya'an",
            '甘孜州': 'Garzê Tibetan Autonomous Prefecture',
            '凉山州': 'Liangshan Yi Autonomous Prefecture',
            '阿坝州': 'Ngawa Tibetan and Qiang Autonomous Prefecture'
        }
    },
    '安徽': {
        'engName': 'Anhui',
        'cities': {
            '亳州': 'Bozhou',
            '六安': "Lu'an",
            '合肥': 'Hefei',
            '安庆': 'Anqing',
            '宣城': 'Xuancheng',
            '宿州': 'Suzhou',
            '巢湖': 'Chaohu',
            '池州': 'Chizhou',
            '淮北': 'Huaibei',
            '淮南': 'Huainan',
            '滁州': 'Chuzhou',
            '芜湖': 'Wuhu',
            '蚌埠': 'Bengbu',
            '铜陵': 'Tongling',
            '阜阳': 'Fuyang',
            '马鞍山': "Ma'anshan",
            '黄山': 'Huangshan'
        }
    },
    '河北': {
        'engName': 'Hebei',
        'cities': {
            '保定': 'Baoding',
            '唐山': 'Tangshan',
            '廊坊': 'Langfang',
            '张家口': 'Zhangjiakou',
            '承德': 'Chengde',
            '沧州': 'Cangzhou',
            '石家庄': 'Shijiazhuang',
            '秦皇岛': 'Qinhuangdao',
            '衡水': 'Hengshui',
            '邢台': 'Xingtai',
            '邯郸': 'Handan'
        }
    },
    '贵州': {
        'engName': 'Guizhou',
        'cities': {
            '六盘水': 'Liupanshui',
            '安顺': 'Anshun',
            '毕节': 'Bijie',
            '贵阳': 'Guiyang',
            '遵义': 'Zunyi',
            '铜仁': 'Tongren',
            '黔东南州': 'Qiandongnan',
            '黔南州': 'Qiannan',
            '黔西南州': 'Qianxinan'
        }
    },
    '甘肃': {
        'engName': 'Gansu',
        'cities': {
            '兰州': 'Lanzhou',
            '嘉峪关': 'Jiayuguan',
            '天水': 'Tianshui',
            '定西': 'Dingxi',
            '平凉': 'Pingliang',
            '庆阳': 'Qingyang',
            '张掖': 'Zhangye',
            '武威': 'Wuwei',
            '甘南': 'Gannan',
            '白银': 'Baiyin',
            '酒泉': 'Jiuquan',
            '金昌': 'Jinchang',
            '陇南': 'Longnan',
            '临夏': 'Linxia'
        }
    },
    '北京': {
        'engName': 'Beijing',
        'cities': {
            '北京': 'Beijing',
            '海淀区': 'Haidian District',
            '朝阳区': 'Chaoyang District',
            '西城区': 'Xicheng District',
            '大兴区': 'Daxing District',
            '丰台区': 'Fengtai District',
            '外地来京人员': 'People from other cities',
            '昌平区': 'Changping District',
            '通州区': 'Tongzhou District',
            '房山区': 'Fangshan District',
            '石景山区': 'Shijingshan District',
            '东城区': 'Dongcheng District',
            '顺义区': 'Shunyi District',
            '怀柔区': 'Huairou District',
            '密云区': 'Miyun District',
            '门头沟区': 'Mentougou District',
            '延庆区': 'Yanqing District'
        }
    },
    '广西': {
        'engName': 'Guangxi',
        'cities': {
            '北海': 'Beihai',
            '南宁': 'Nanning',
            '崇左': 'Chongzuo',
            '来宾': 'Laibin',
            '柳州': 'Liuzhou',
            '桂林': 'Guilin',
            '梧州': 'Wuzhou',
            '河池': 'Hechi',
            '玉林': 'Yulin',
            '百色': 'Baise',
            '贵港': 'Guigang',
            '贺州': 'Hezhou',
            '钦州': 'Qinzhou',
            '防城港': 'Fangchenggang'
        }
    },
    '湖北': {
        'engName': 'Hubei',
        'cities': {
            '十堰': 'Shiyan',
            '咸宁': 'Xianning',
            '孝感': 'Xiaogan',
            '宜昌': 'Yichang',
            '恩施': 'Enshi',
            '武汉': 'Wuhan',
            '荆州': 'Jingzhou',
            '荆门': 'Jingmen',
            '襄阳': 'Xiangyang',
            '仙桃': 'Xiantao',
            '天门': 'Tianmen',
            '襄樊': 'Xiangfan',
            '鄂州': 'Ezhou',
            '随州': 'Suizhou',
            '黄冈': 'Huanggang',
            '黄石': 'Huangshi',
            '恩施州': 'Enshi Tujia and Miao Autonomous Prefecture',
            '潜江': 'Qianjiang',
            '神农架林区': 'Shennongjia'
        }
    },
    '江苏': {
        'engName': 'Jiangsu',
        'cities': {
            '南京': 'Nanjing',
            '南通': 'Nantong',
            '宿迁': 'Suqian',
            '常州': 'Changzhou',
            '徐州': 'Xuzhou',
            '扬州': 'Yangzhou',
            '无锡': 'Wuxi',
            '泰州': 'Taizhou',
            '淮安': 'Huainan',
            '盐城': 'Yancheng',
            '苏州': 'Suzhou',
            '连云港': 'Lianyungang',
            '镇江': 'Zhenjiang'
        }
    },
    '吉林': {
        'engName': 'Jilin',
        'cities': {
            '吉林市': 'Jilin',
            '四平市': 'Siping',
            '延边': 'Yanbian',
            '松原': 'Songyuan',
            '白城': 'Baicheng',
            '白山': 'Baishan',
            '辽源': 'Liaoyuan',
            '通化': 'Tonghua',
            '长春': 'Changchun',
            '公主岭': 'Gongzhuling',
            '梅河口': 'Meihekou'
        }
    },
    '陕西': {
        'engName': 'Shanxi',
        'cities': {
            '咸阳': 'Xianyang',
            '商洛': 'Shangluo',
            '安康': 'Ankang',
            '宝鸡': 'Baoji',
            '延安': "Yan'an",
            '榆林': 'Yulin',
            '汉中': 'Hanzhong',
            '渭南': 'Weinan',
            '西安': "Xi'an",
            '铜川': 'Tongchuan',
            '杨凌': 'Yangling District in Xianyang',
            '韩城': 'Hancheng'
        }
    },
    '天津': {
        'engName': 'Tianjin',
        'cities': {
            '天津': 'Tianjin',
            '宝坻区': 'Baodi District',
            '河东区': 'Hedong District',
            '河北区': 'Hebei District',
            '北辰区': 'Beichen District',
            '南开区': 'Nankai District',
            '外地来津人员': 'People from other cities',
            '和平区': 'Heping District',
            '宁河区': 'Ninghe District',
            '东丽区': 'Dongli District',
            '滨海新区': 'Binhai New Area',
            '河西区': 'Hexi District',
            '西青区': 'Xiqing District',
            '武清区': 'Wuqing District',
            '津南区': 'Jinnan District',
            '红桥区': 'Hongqiao District',
        }
    },
    '湖南': {
        'engName': 'Hunan',
        'cities': {
            '娄底': 'Loudi',
            '岳阳': 'Yueyang',
            '常德': 'Changde',
            '张家界': 'Zhangjiajie',
            '怀化': 'Huaihua',
            '株洲': 'Zhuzhou',
            '永州': 'Yongzhou',
            '湘潭': 'Xiangtan',
            '湘西自治州': 'Xiangxi',
            '益阳': 'Yiyang',
            '衡阳': 'Hengyang',
            '邵阳': 'Shaoyang',
            '郴州': 'Chenzhou',
            '长沙': 'Changsha'
        }
    },
    '西藏': {
        'engName': 'Xizang',
        'cities': {
            '山南': 'Shannan',
            '拉萨': 'Lhasa',
            '日喀则': 'Shigatse',
            '昌都': 'Chamdo',
            '林芝': 'Nyingchi',
            '那曲': 'Naqu',
            '阿里': 'Ali'
        }
    },
    '青海': {
        'engName': 'Qinghai',
        'cities': {
            '果洛': 'Guoluo',
            '海东': 'Haidong',
            '海北州': 'Haibei',
            '海南': 'Hainan',
            '海西': 'Haixi',
            '玉树': 'Yushu',
            '西宁': 'Xining',
            '黄南': 'Huangnan'
        }
    },
    '重庆': {
        'engName': 'Chongqing',
        'cities': {
            '重庆': 'Chongqing',
            '万州区': 'Wanzhou District',
            '江北区': 'Jiangbei District',
            '綦江区': 'Qijiang District',
            '合川区': 'Hechuan District',
            '九龙坡区': 'Jiulongpo District',
            '垫江县': 'Dianjiang County',
            '渝中区': 'Yuzhong District',
            '奉节县': 'Fengjie County',
            '潼南区': 'Tongnan District',
            '两江新区': 'Liangjiang New Area',
            '南岸区': "Nan'an District",
            '大足区': 'Dazu District',
            '忠县': 'Zhong County',
            '长寿区': 'Changshou District',
            '渝北区': 'Yubei District',
            '石柱县': 'Shizhu Tujia Autonomous County',
            '荣昌区': 'Rongchang District',
            '丰都县': 'Fengdu County',
            '铜梁区': 'Tongliang District',
            '沙坪坝区': 'Shapingba District',
            '云阳县': 'Yunyang County',
            '开州区': 'Kaizhou District',
            '巫溪县': 'Wuxi County',
            '巫山县': 'Wushan County',
            '巴南区': 'Banan District',
            '璧山区': 'Bishan District',
            '大渡口区': 'Dadukou District',
            '永川区': 'Yongchuan District',
            '高新区': 'Chongqing High-tech Zone',
            '江津区': 'Jiangjin District',
            '涪陵区': 'Fuling District',
            '彭水县': 'Pengshui Miao and Tujia Autonomous County',
            '武隆区': 'Wulong District',
            '酉阳县': 'Youyang Tujia and Miao Autonomous County',
            '万盛经开区': 'Wansheng District',
            '梁平区': 'Liangping District',
            '黔江区': 'Qianjiang Tujia and Miao Autonomous County',
            '城口县': 'Chengkou County',
            '秀山县': 'Xiushan Tujia and Miao Autonomous County'
        }
    },
    '香港': {
        'engName': 'Hong Kong'
    },
    '澳门': {
        'engName': 'Macau'
    },
    '台湾': {
        'engName': 'Tai Wan'
    }
}