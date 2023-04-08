# getweather方法
>*Weather* 类
>> 参数  
>>>***self.url*** -> str  
>>>*指定数据获取api接口*  
>>
>>>***self.st_date*** -> str  
>>>*天气获取开始年月格式为* *YYYY-MM*
>>
>>>***self.count*** -> int  
>>> *天气持续月数，默认值为* *1*  
>>
>>>***self.weathers*** -> dict  
>>>*以嵌套字典形式存储获取到的天气数据，初值为空*  
>>>*字典格式为*  
>>>```
>>>{
>>>date:{ 
>>>     'weather': value,
>>>     'rainfall': value
>>> }
>>>```
>
>>函数
>>>***self.check(self)*** -> None  
>>>*检查传入参数正确性，抛出异常*
>>
>>>***change(self, num: int)*** -> str  
>>> *转化日期数据时期满足* *YYYY-DD* *格式并可向后迭代*
>>
>>>***get_history_weather(self)*** -> dict  
>>>*返回值为 **self.weathers** 爬取数据至本地进行简单的 json 格式化处理*  
>>>*调用 **date_with_weather** 进一步处理数据*
>>
>>>***date_with_weather(self, dt, wt)*** -> None  
>>>*对取得的数据进行进一步处理，将日期与对应天气与降水相关联，赋值给 **self.weather** *
>>
>>>***get_adcode*** -> None  
>>>*搜索adcode字典对 **self.adcode**  赋值，模糊检索匹配地区*

> ~~*Area_code* 类~~