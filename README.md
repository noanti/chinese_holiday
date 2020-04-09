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

day = datetime.datetime(2018, 12, 27)
while day < datetime.datetime(2019, 1, 4):
    print('{} is_holiday: {} is_tiaoxiu: {} is_rest:{}'.format(
        day.strftime('%Y-%m-%d'), is_holiday(day), is_tiaoxiu(day), is_rest(day)
    ))
    day = day + datetime.timedelta(days=1)
```
```
2018-12-27 is_holiday: (False, None) is_tiaoxiu: (False, None) is_rest:False
2018-12-28 is_holiday: (False, None) is_tiaoxiu: (False, None) is_rest:False
2018-12-29 is_holiday: (False, None) is_tiaoxiu: (True, '元旦') is_rest:False
2018-12-30 is_holiday: (True, '元旦') is_tiaoxiu: (False, None) is_rest:True
2018-12-31 is_holiday: (True, '元旦') is_tiaoxiu: (False, None) is_rest:True
2019-01-01 is_holiday: (True, '元旦') is_tiaoxiu: (False, None) is_rest:True
2019-01-02 is_holiday: (False, None) is_tiaoxiu: (False, None) is_rest:False
2019-01-03 is_holiday: (False, None) is_tiaoxiu: (False, None) is_rest:False
```

## 注意
1. 有几年的国庆和中秋假期是相连的，在实际数据分析中区分这两种假的意义不大，也不好区分
所以提供了一个新的"国庆+中秋"假期类型。
2. 有的假期可能与周末相连，这里认为该周末也属于假期期间。
3. 调休(is_tiaoxiu)的含义为本该休息但因假期安排改成上班的日子。
