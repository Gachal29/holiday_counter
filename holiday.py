import datetime
import calendar
import jpholiday
import re


class Counter:
    def __init__(self, year: int=datetime.datetime.today().year, start_month: int=4):
        self.year: int = year
        self.start_month: int = start_month
        
        self.calendar: dict[str, tuple[int, int]] = {}

        cal: calendar.Calendar = calendar.Calendar()

        for month in range(start_month, 13):
            self.calendar[f"{self.year}_{month}"] = cal.monthdays2calendar(year=self.year, month=month)

        for month in range(1, start_month):
            if month == 1:
                self.year += 1
            
            self.calendar[f"{self.year}_{month}"] = cal.monthdays2calendar(self.year, month)

    def count(self, holidays: list=[5, 6]):
        # day_of_week = ["月", "火", "水", "木", "金", "土", "日"]
        self.holiday_num = 0
        month_keys = self.calendar.keys()

        for month in month_keys:
            month_calendar = self.calendar[month]
            for week in month_calendar:
                for day in week:
                    if day[0] == 0:
                        continue

                    date = datetime.date(int(month[:month.index("_")]), int(month[month.index("_")+1:]), day[0])
                    # date_str = date.strftime("%Y年%m月%d日")
                    if day[1] in holidays:
                        self.holiday_num += 1
                        # print(f"{self.holiday_num}: {date_str}({day_of_week[day[1]]})")
                        continue

                    if jpholiday.is_holiday(date):
                        self.holiday_num += 1
                        # print(f"{self.holiday_num}: {date_str}({day_of_week[day[1]]}) {jpholiday.is_holiday_name(date)}")

    def display_info(self):
        print("カレンダー休日数：", self.holiday_num)



if __name__ == "__main__":
    year = input('調べたい年数を入力してください：')
    if re.search("\d{4}", year):
        year = int(year)
    else:
        raise ValueError("年数を正しく入力してください。")
    
    start_month = int(input('開始月を入力してください：'))
    if not start_month >= 1 and start_month <= 12:
        raise ValueError("開始月を正しく入力してください。")

    counter = Counter(year=year, start_month=start_month)
    counter.count()
    counter.display_info()
