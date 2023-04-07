import json
import re

import jsonpath
import requests


class Weather:
    """天气处理类
    Attributes:
        url -> (str): api接口
        st_date -> (str): 开始日期(精确至月）格式为 YYYY-MM
        count -> int: 持续月数
    """

    def __init__(self, st_date, count=1, adcode=None) -> None:
        self.url = 'https://hz.hjhj-e.com/api/index/calendar/'
        self.st_date = st_date
        self.adcode = adcode
        self.count = count
        self.weathers = dict()
        self.check()

    def check(self):
        pattern = r'^\d{4}-(0[1-9]|1[0-2])$'
        if not re.match(pattern, self.st_date) or self.adcode is None:
            raise Exception("st_date or adcode value error,st_date type like YYYY-MM")
        try:
            if self.count <= 0:
                raise Exception("count value error")
        except TypeError:
            Exception("count value error")
        return None

    def change(self, num: int) -> str:
        year = int(self.st_date[0:4])
        month = int(self.st_date[-2:])
        year += num // 12
        month += num % 12
        if month > 12:
            raise Exception("month value error")
        if month > 12:
            year = str(year - 1)
            month = month - 12
        if month < 10:
            month = '0' + str(month)
        return f'{year}-{month}'

    def get_history_weather(self) -> dict:
        for i in range(self.count):
            date = self.change(i)
            get_url = f'{self.url}{date}/{self.adcode}'
            req = requests.get(url=get_url)
            req.encoding = 'utf-8'
            data = json.loads(req.text)
            weathers_data = jsonpath.jsonpath(data, '$..data')
            self.date_with_weather(date, weathers_data[0])
        return self.weathers

    def date_with_weather(self, dt: str, wt: dict):
        for i in wt.keys():
            date = f'{dt}-{i[1:] if len(i[1:]) == 2 else "0" + i[1:]}'
            if wt[i] != {}:
                self.weathers[date] = {
                    "weather": wt[i]['weather'],
                    "rainfall": wt[i]['rainfall']
                }
        return None


class Area_code:
    """行政区划获取类
    Attributes:
        url -> (str): api地址
        key -> (str): api认证
        keywords ->(str): 地名关键词
        subdistrict -> (str): 设置显示下级行政区级数,可选值：0、1、2、3
        page -> (str): 需要第几页数据,最外层的districts最多会返回20个数据，若超过限制，请用page请求下一页数据。
        output ->(str): 返回数据格式类型,可选值：JSON，XML
    """

    def __init__(self):
        self.url = 'https://restapi.amap.com/v3/config/district?'
        self.key = '157b68bc8bc8f2345294b4dfb97c5afc'
        self.keywords = ''
        self.subdistrict = '3'
        self.page = '1'
        self.output = 'JSON'

    def get_code(self):
        get_url = f'{self.url}key={self.key}&keywords={self.keywords}&subdistrict={self.subdistrict}' \
                  f'&page={self.page}&output={self.output}'
        req = requests.get(url=get_url)
        req.encoding = 'utf-8'
        data = json.loads(req.text)
        adcode = jsonpath.jsonpath(data, '$..adcode')
        address = jsonpath.jsonpath(data, '$..name')
        level = jsonpath.jsonpath(data, '$..level')
        res = []
        for code, ad, lv in zip(adcode, address, level):
            if lv != 'street':
                res.append((code, ad, lv))
        return res

