from getweather import Area_code, Weather
import pprint


def demo():
    codes = Area_code()
    # 查找地区
    codes.keywords = '南浔'
    # 取得地区区划编码
    code = codes.get_code()[0][0]
    weathers = Weather('2020-09', 3, code)
    dic = weathers.get_history_weather()
    key = dic.keys()
    res = dict()
    for x in key:
        try:
            weather = dic[x]['weather']
            rainfall = dic[x]['rainfall']
            res[x] = {'weather': weather, 'rainfall': rainfall}
        except:
            continue
    pprint.pprint(dic)


if __name__ == '__main__':
    demo()
