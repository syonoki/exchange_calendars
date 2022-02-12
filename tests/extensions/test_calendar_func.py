from unittest import TestCase

import pandas as pd
import pandas.testing as pdt

from commonutils.datetime.date_func import to_timestamp
from exchange_calendars.extensions.calendar_func import get_biz_dates, find_valid_start_end_dates, special_holidays, \
    find_closest_date_after, find_closest_date_before
from exchange_calendars.extensions.exchange_calendar_krx import KRXExchangeCalendar


class TestCalendarFuncs(TestCase):

    def test_get_biz_dates_without_tz(self):
        cal = KRXExchangeCalendar()
        start = '2018-01-01'
        end = '2018-01-06'

        expected = pd.DatetimeIndex(
            ['2018-01-02', '2018-01-03', '2018-01-04', '2018-01-05'])

        result = get_biz_dates(cal, start, end)
        pdt.assert_index_equal(expected, result)

    def test_get_biz_dates_with_tz(self):
        cal = KRXExchangeCalendar()
        start = '2018-01-01'
        end = '2018-01-06'

        expected = pd.DatetimeIndex(
            ['2018-01-02', '2018-01-03', '2018-01-04', '2018-01-05'], tz='UTC')

        result = get_biz_dates(cal, start, end, with_tz=True)
        pdt.assert_index_equal(expected, result)

    def test_find_valid_start_end_dates_with_tz(self):
        cal = KRXExchangeCalendar()
        start = '2018-01-01'
        end = '2018-01-06'

        result_start, result_end = find_valid_start_end_dates(cal, start, end, tz='UTC')
        self.assertEqual(pd.Timestamp('2018-01-02', tz='UTC'), result_start)
        self.assertEqual(pd.Timestamp('2018-01-05', tz='UTC'), result_end)

    def test_find_valid_start_end_dates_without_tz(self):
        cal = KRXExchangeCalendar()
        start = '2018-01-01'
        end = '2018-01-06'

        result_start, result_end = find_valid_start_end_dates(cal, start, end)
        self.assertEqual(pd.Timestamp('2018-01-02'), result_start)
        self.assertEqual(pd.Timestamp('2018-01-05'), result_end)

    def test_special_holidays_string_date(self):
        cal = KRXExchangeCalendar()

        expected = pd.DatetimeIndex(['2018-02-15', '2018-02-16', '2018-02-17'])
        start = '2018-02-01'
        end = '2018-02-18'

        result = special_holidays(cal, start, end)

        pdt.assert_index_equal(expected, result)

    def test_special_holidays_tz_naive_timestamp(self):
        cal = KRXExchangeCalendar()

        expected = pd.DatetimeIndex(['2018-02-15', '2018-02-16', '2018-02-17'])
        start = pd.Timestamp('2018-02-01')
        end = pd.Timestamp('2018-02-18')

        result = special_holidays(cal, start, end)

        pdt.assert_index_equal(expected, result)

    def test_find_closest_date_after_shift(self):
        calendar = KRXExchangeCalendar()
        biz_dates = get_biz_dates(calendar)

        start_date = '2017-01-01'

        date = find_closest_date_after(start_date, biz_dates)

        self.assertEqual(to_timestamp('2017-01-02'), date)

    def test_find_closest_date_after_exact(self):
        calendar = KRXExchangeCalendar()
        biz_dates = get_biz_dates(calendar)

        start_date = '2017-01-03'

        date = find_closest_date_after(start_date, biz_dates)

        self.assertEqual(to_timestamp('2017-01-03'), date)

    def test_find_closest_date_before_shift(self):
        calendar = KRXExchangeCalendar()
        biz_dates = get_biz_dates(calendar)

        end_date = '2017-01-01'

        date = find_closest_date_before(end_date, biz_dates)

        self.assertEqual(to_timestamp('2016-12-29'), date)

    def test_find_closest_date_before_exact(self):
        calendar = KRXExchangeCalendar()
        biz_dates = get_biz_dates(calendar)

        start_date = '2016-12-28'

        date = find_closest_date_after(start_date, biz_dates)

        self.assertEqual(to_timestamp('2016-12-28'), date)
