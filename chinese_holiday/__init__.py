import datetime
from os import path

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
            start = datetime.datetime.strptime(start, '%Y%m%d')
            end = datetime.datetime.strptime(end, '%Y%m%d')
            date = start
            while date <= end:
                self.holidays[date] = arrangement['id']
                date = date + datetime.timedelta(days=1)
            for date in arrangement['tiaoxiu']:
                date = datetime.datetime.strptime(date, '%Y%m%d')
                self.tiaoxiu[date] = arrangement['id']

    @classmethod
    def load(cls, data_path):
        with open(data_path) as f:
            data = yaml.safe_load(f)
        festivals = data['festivals']
        arrangements = data['arrangements']
        return cls(festivals, arrangements)

    def is_holiday(self, date):
        if date in self.holidays:
            return True, self.festival_map[self.holidays[date]]
        else:
            return False, None

    def is_tiaoxiu(self, date):
        if date in self.tiaoxiu:
            return True, self.festival_map[self.tiaoxiu[date]]
        else:
            return False, None

    def is_rest(self, date):
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
    day = datetime.datetime(2018, 12, 27)
    while day < datetime.datetime(2019, 1, 4):
        print('{} is_holiday: {} is_tiaoxiu: {} is_rest:{}'.format(
            day.strftime('%Y-%m-%d'), is_holiday(day), is_tiaoxiu(day), is_rest(day)
        ))
        day = day + datetime.timedelta(days=1)

