from unittest import TestCase

import pandas as pd
import pandas.testing as pdt

from exchange_calendars.extensions.calendar_extension import GenericExchangeCalendar


class ExtendedTradingCalendarTestCase(TestCase):

    def setUp(self):
        self.holidays = [
            pd.Timestamp(2019, 1, 1),
            pd.Timestamp(2019, 1, 2),
            pd.Timestamp(2019, 1, 3),
            pd.Timestamp(2019, 1, 8),
            pd.Timestamp(2019, 1, 31),
        ]

        self.calendar = GenericExchangeCalendar('TestCal', holidays=self.holidays)

    def test_valid_session_or_next_invalid_date(self):
        result = self.calendar.valid_session_or_next('2019-01-02')

        self.assertEqual(result, pd.Timestamp('2019-01-04', tz='utc'))

    def test_valid_session_or_next_valid_date(self):
        result = self.calendar.valid_session_or_next('2019-01-04')

        self.assertEqual(result, pd.Timestamp('2019-01-04', tz='utc'))

    def test_valid_session_or_previous_invalid_date(self):
        result = self.calendar.valid_session_or_previous('2019-01-08')

        self.assertEqual(result, pd.Timestamp('2019-01-07', tz='utc'))

    def test_valid_session_or_previous_valid_date(self):
        result = self.calendar.valid_session_or_previous('2019-01-07')

        self.assertEqual(result, pd.Timestamp('2019-01-07', tz='utc'))

    def test_month_ends_in_range(self):
        start = '2019-01'
        end = '2019-03'

        result = self.calendar.month_ends_in_range(start, end, days_offset=2)

        expected = pd.DatetimeIndex(
            [pd.Timestamp('2019-01-28', tz='utc'),
             pd.Timestamp('2019-02-26', tz='utc'),
             pd.Timestamp('2019-03-27', tz='utc')])
        pdt.assert_index_equal(result, expected)

    def test_month_starts_in_range(self):
        start = '2019-01'
        end = '2019-03'

        result = self.calendar.month_starts_in_range(start, end, days_offset=2)

        expected = pd.DatetimeIndex(
            [pd.Timestamp('2019-01-09', tz='utc'),
             pd.Timestamp('2019-02-05', tz='utc'),
             pd.Timestamp('2019-03-05', tz='utc')])
        pdt.assert_index_equal(result, expected)

    def test_week_ends_in_range(self):
        start = '2019-01-01'
        end = '2019-01-31'

        result = self.calendar.week_ends_in_range(start, end, days_offset=0)

        expected = pd.DatetimeIndex(
            [pd.Timestamp('2019-01-04', tz='utc'),
             pd.Timestamp('2019-01-11', tz='utc'),
             pd.Timestamp('2019-01-18', tz='utc'),
             pd.Timestamp('2019-01-25', tz='utc'),
             pd.Timestamp('2019-02-01', tz='utc')])
        pdt.assert_index_equal(result, expected)

    def test_week_starts_in_range(self):
        start = '2019-01-01'
        end = '2019-01-31'

        result = self.calendar.week_starts_in_range(start, end, days_offset=0)

        expected = pd.DatetimeIndex(
            [pd.Timestamp('2018-12-31', tz='utc'),
             pd.Timestamp('2019-01-07', tz='utc'),
             pd.Timestamp('2019-01-14', tz='utc'),
             pd.Timestamp('2019-01-21', tz='utc'),
             pd.Timestamp('2019-01-28', tz='utc')])
        pdt.assert_index_equal(result, expected)

    def test_quarter_ends_in_range(self):
        start = '2Q2018'
        end = '1Q2019'

        result = self.calendar.quarter_ends_in_range(start, end, days_offset=2)

        expected = pd.DatetimeIndex(
            [pd.Timestamp('2018-06-27', tz='utc'),
             pd.Timestamp('2018-09-26', tz='utc'),
             pd.Timestamp('2018-12-27', tz='utc'),
             pd.Timestamp('2019-03-27', tz='utc')
             ])
        pdt.assert_index_equal(result, expected)

    def test_quarter_starts_in_range(self):
        start = '2Q2018'
        end = '1Q2019'

        result = self.calendar.quarter_starts_in_range(start, end, days_offset=2)

        expected = pd.DatetimeIndex(
            [pd.Timestamp('2018-04-04', tz='utc'),
             pd.Timestamp('2018-07-04', tz='utc'),
             pd.Timestamp('2018-10-03', tz='utc'),
             pd.Timestamp('2019-01-09', tz='utc')
             ])
        pdt.assert_index_equal(result, expected)
