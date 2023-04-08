import json
import re
import difflib
import logging

import jsonpath
import requests

from adcode_dic import Adcode

logging.basicConfig(level=logging.INFO)
logging.disable()


class Weather:
    """天气处理类
    Attributes:
        url -> (str): api接口
        st_date -> (str): 开始日期(精确至月）格式为 YYYY-MM
        count -> int: 持续月数
        weathers -> dict: 获取到的天气信息
    """

    def __init__(self, st_date, address, count=1) -> None:
        self.url = 'https://hz.hjhj-e.com/api/index/calendar/'
        self.st_date = st_date
        self.adcode = None
        self.get_adcode(address)
        self.count = count
        self.weathers = dict()
        self.check()

    def check(self):
        pattern = r'^\d{4}-(0[1-9]|1[0-2])$'
        if not re.match(pattern, self.st_date):
            raise Exception("st_date value error,st_date type like YYYY-MM")
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
            logging.info(self.adcode)
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

    def get_adcode(self, ad):
        dic_code = Adcode().get()
        ads = dic_code.keys()
        choose = difflib.get_close_matches(ad, ads, 3, cutoff=0.6)
        logging.info(choose)
        if len(choose) == 0:
            raise Exception('address not found')
        if len(choose) > 1:
            print('存在多个匹配值')
            for i in range(len(choose)):
                print('%5s' % (str(i) + '.') + str(choose[i]))
            x = int(input("choose:"))
            choose = choose[x]
        else:
            choose = choose[0]
        logging.info(dic_code[choose])
        self.adcode = dic_code[choose]
        return None


