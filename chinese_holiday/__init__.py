import datetime
from os import path
from io import open

import yaml

__all__ = ['is_holiday', 'is_tiaoxiu', 'is_rest']

PATH = path.dirname(__file__)
DATA_FILENAME = 'festival_arrangements.yaml'
DATA_PATH = path.join(PATH, DATA_FILENAME)


class ChineseHoliday:
    def __init__(self, festivals, arrangements):
        self.festival_map = {festival['id']: festival['name'] for festival in festivals}
        self.holidays = {}
        self.tiaoxiu = {}
        for arrangement in arrangements:
            start, end = arrangement['range'].split('-')
            start = datetime.datetime.strptime(start, '%Y%m%d').date()
            end = datetime.datetime.strptime(end, '%Y%m%d').date()
            date = start
            while date <= end:
                self.holidays[date] = arrangement['id']
                date = date + datetime.timedelta(days=1)
            for date in arrangement['tiaoxiu']:
                date = datetime.datetime.strptime(date, '%Y%m%d').date()
                self.tiaoxiu[date] = arrangement['id']

    @classmethod
    def load(cls, data_path):
        with open(data_path, encoding='utf-8') as f:
            data = yaml.safe_load(f)
        festivals = data['festivals']
        arrangements = data['arrangements']
        return cls(festivals, arrangements)

    def is_holiday(self, date):
        if isinstance(date, datetime.datetime):
            date = date.date()
        if date in self.holidays:
            return True, self.festival_map[self.holidays[date]]
        else:
            return False, None

    def is_tiaoxiu(self, date):
        if isinstance(date, datetime.datetime):
            date = date.date()
        if date in self.tiaoxiu:
            return True, self.festival_map[self.tiaoxiu[date]]
        else:
            return False, None

    def is_rest(self, date):
        if isinstance(date, datetime.datetime):
            date = date.date()
        if date in self.holidays:
            return True
        elif date in self.tiaoxiu:
            return False
        else:
            return date.weekday() in (5, 6)


holiday_helper = ChineseHoliday.load(DATA_PATH)
is_holiday = holiday_helper.is_holiday
is_tiaoxiu = holiday_helper.is_tiaoxiu
is_rest = holiday_helper.is_rest


if __name__ == '__main__':
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

