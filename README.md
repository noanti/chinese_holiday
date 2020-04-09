## 中国假期安排
根据[chinese-calendar](https://github.com/LKI/chinese-calendar)的规则文件把历年假期安排整理成了yaml格式，方便不同语言直接解析使用。

详见[festival_arrangements.yaml](https://github.com/noanti/chinese_holiday/blob/master/chinese_holiday/festival_arrangements.yaml)

附带了python的解析实现。

## 安装
```
pip install git+https://github.com/noanti/chinese_holiday.git@master
```

## 使用
```python
import datetime
from chinese_holiday import is_tiaoxiu, is_rest, is_holiday

# 以2018年为例
# http://www.gov.cn/zhengce/content/2017-11/30/content_5243579.htm
# 一、元旦：1月1日放假，与周末连休。
# 二、春节：2月15日至21日放假调休，共7天。2月11日（星期日）、2月24日（星期六）上班。
# 三、清明节：4月5日至7日放假调休，共3天。4月8日（星期日）上班。
# 四、劳动节：4月29日至5月1日放假调休，共3天。4月28日（星期六）上班。
# 五、端午节：6月18日放假，与周末连休。
# 六、中秋节：9月24日放假，与周末连休。
# 七、国庆节：10月1日至7日放假调休，共7天。9月29日（星期六）、9月30日（星期日）上班。

holiday, holiday_name = is_holiday(datetime.date(2017, 12, 29))  # False, None
holiday, holiday_name = is_holiday(datetime.date(2017, 12, 30))  # True, '元旦'
holiday, holiday_name = is_holiday(datetime.date(2017, 12, 31))  # True, '元旦'
holiday, holiday_name = is_holiday(datetime.date(2018, 1, 1))  # True, '元旦'
holiday, holiday_name = is_holiday(datetime.date(2018, 1, 2))  # False, None

day = datetime.date(2018, 2, 11)
while day <= datetime.date(2018, 2, 24):
    print('{} is_holiday: {} is_tiaoxiu: {} is_rest:{}'.format(
        day.strftime('%Y-%m-%d'), is_holiday(day), is_tiaoxiu(day), is_rest(day)
    ))
    day = day + datetime.timedelta(days=1)
```
```
2018-02-11 is_holiday: (False, None) is_tiaoxiu: (True, '春节') is_rest:False
2018-02-12 is_holiday: (False, None) is_tiaoxiu: (False, None) is_rest:False
2018-02-13 is_holiday: (False, None) is_tiaoxiu: (False, None) is_rest:False
2018-02-14 is_holiday: (False, None) is_tiaoxiu: (False, None) is_rest:False
2018-02-15 is_holiday: (True, '春节') is_tiaoxiu: (False, None) is_rest:True
2018-02-16 is_holiday: (True, '春节') is_tiaoxiu: (False, None) is_rest:True
2018-02-17 is_holiday: (True, '春节') is_tiaoxiu: (False, None) is_rest:True
2018-02-18 is_holiday: (True, '春节') is_tiaoxiu: (False, None) is_rest:True
2018-02-19 is_holiday: (True, '春节') is_tiaoxiu: (False, None) is_rest:True
2018-02-20 is_holiday: (True, '春节') is_tiaoxiu: (False, None) is_rest:True
2018-02-21 is_holiday: (True, '春节') is_tiaoxiu: (False, None) is_rest:True
2018-02-22 is_holiday: (False, None) is_tiaoxiu: (False, None) is_rest:False
2018-02-23 is_holiday: (False, None) is_tiaoxiu: (False, None) is_rest:False
2018-02-24 is_holiday: (False, None) is_tiaoxiu: (True, '春节') is_rest:False
```

## 注意
1. 有几年的国庆和中秋假期是相连的，在实际数据分析中区分这两种假的意义不大，也不好区分
所以提供了一个新的"国庆+中秋"假期类型。
2. 有的假期可能与周末相连，这里认为该周末也属于假期期间。
3. 调休(is_tiaoxiu)的含义为本该休息但因假期安排改成上班的日子。
