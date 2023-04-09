from getweather import Weather
import pprint


def demo():
    weathers = Weather('2021-03', '北京', 3)
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
