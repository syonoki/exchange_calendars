from commonutils.datetime import yesterday
from datetime import datetime
from commonutils.datetime.date_func import normalized_today
yest = yesterday()
yest = datetime(yest.year, yest.month, yest.day)
today = normalized_today()

from exchange_calendars.extensions.exchange_calendar_krx import KRXExchangeCalendar
cal = KRXExchangeCalendar()

kr_prev_bizdate = cal.previous_session_label('2012-07-02', today)

if __name__ == '__main__':
    print(kr_prev_bizdate)