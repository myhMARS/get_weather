from getweather import Area_code, Weather
import pprint


def demo():
    codes = Area_code('湖州')
    # 取得地区区划编码
    code = codes.get_code()[0]
    print(f'天气位置: {code[1]}')
    weathers = Weather('2020-09', 3, code[0])
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
