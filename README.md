## 中国假期安排
根据[chinese-calendar](https://github.com/LKI/chinese-calendar)的规则文件把历年假期安排整理成了yaml格式，方便不同语言直接解析使用。
详见[festival_arrangements.yaml](https://github.com/noanti/chinese_holiday.git/blob/master/chinese_holiday/festival_arrangements.yaml)

附带了python的解析实现。

## 安装
```
pip install git+https://github.com/noanti/chinese_holiday.git@master
```

## 使用
```python
from chinese_holiday import is_tiaoxiu, is_rest, is_holiday
```

## 注意
1. 有几年的国庆和中秋假期是相连的，在实际数据分析中区分这两种假的意义不大，也不好区分
所以提供了一个新的"国庆+中秋"假期类型。
2. 有的假期可能与周末相连，则认为该周末也属于假期期间。
3. 调休(is_tiaoxiu)的含义为本该休息但因假期安排改成上班的日子。
