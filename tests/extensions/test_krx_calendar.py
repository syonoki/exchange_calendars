from unittest import TestCase

import pandas as pd

from exchange_calendars.extensions.exchange_calendar_krx import KRXExchangeCalendar


class KRXCalendarTestCase(TestCase):
    MAX_SESSION_HOURS = 8.5

    def test_2017_holidays(self):
        # lunar new years: jan 27, 30
        # independence day: mar 1
        # labor day: may 1
        # buddhas birthday: may 3
        # children's day: may 5
        # president: may 9
        # memorial day: jun 6
        # liberation day: aug 15
        # substitution holiday: oct 2
        # harvest mood day: oct, 3, 4, 5, 6
        # hangul proclamation day: oct 9
        # christmas :dec 25
        # end year closing: dec 29
        self.calendar = KRXExchangeCalendar()

        for day in ['2017-01-27', '2017-01-30', '2017-03-01', '2017-05-01', '2017-05-03',
                    '2017-05-05', '2017-05-09', '2017-06-06', '2017-08-15', '2017-10-02',
                    '2017-10-03', '2017-10-04', '2017-10-05', '2017-10-06', '2017-10-09',
                    '2017-12-25', '2017-12-29']:
            self.assertFalse(self.calendar.is_session(pd.Timestamp(day, tz='UTC')))
