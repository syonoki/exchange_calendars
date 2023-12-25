from abc import ABC
from datetime import time
from functools import lru_cache

import pandas as pd
from exchange_calendars.extensions.calendar_func import coerce_string_to_quarter_period
from pytz import timezone
from exchange_calendars import ExchangeCalendar

from commonutils.input_validation import coerce_string
from commonutils.preprocess import preprocess

MAX_MONTH_RANGE = 23
MAX_WEEK_RANGE = 5
MAX_QUARTER_RANGE = 69


def _out_of_range_error(a, b=None, var='offset'):
    start = 0
    if b is None:
        end = a - 1
    else:
        start = a
        end = b - 1
    return ValueError(
        '{var} must be in between {start} and {end} inclusive'.format(
            var=var,
            start=start,
            end=end,
        )
    )


class ExtendedExchangeCalendar(ExchangeCalendar, ABC):

    # <editor-fold desc="Business days">
    def _periods(self, period_field, offset):
        sessions = self.all_sessions
        period = getattr(sessions, period_field)
        if period_field == 'week':
            return pd.Series(sessions, index=sessions).groupby([pd.Grouper(freq='W')]).nth(offset)
        elif period_field == 'quarter':
            return pd.Series(sessions, index=sessions).groupby([pd.Grouper(freq='BQS')]).nth(offset)
        else:
            return pd.Series(sessions).groupby([sessions.year, period]).nth(offset)

    def _months_in_range(self, start, end, n, invert):
        if not 0 <= n < MAX_MONTH_RANGE:
            raise _out_of_range_error(MAX_MONTH_RANGE)
        if invert:
            days_offset = -n - 1
        else:
            days_offset = n

        month_ends = self._periods('month', days_offset)

        if int(pd.__version__[0]) == 2:
            month_ends = month_ends.reset_index(drop=True)
            idx_start = month_ends[(month_ends.dt.year == start.year) & (month_ends.dt.month == start.month)].index[0]
            idx_end = month_ends[(month_ends.dt.year == end.year) & (month_ends.dt.month == end.month)].index[0]
            return pd.DatetimeIndex(month_ends[idx_start: idx_end + 1])
        else:
            idx_start = month_ends.index.get_locs([start.year, start.month])[0]
            idx_end = month_ends.index.get_locs([end.year, end.month])[0]
            return pd.DatetimeIndex(month_ends[idx_start: idx_end + 1])

    # @preprocess(start=coerce_string(pd.Period), end=coerce_string(pd.Period))
    def month_ends_in_range(self, start, end, days_offset=0):
        return self._months_in_range(start, end, days_offset, invert=True)

    # @preprocess(start=coerce_string(pd.Period), end=coerce_string(pd.Period))
    def month_starts_in_range(self, start, end, days_offset=0):
        return self._months_in_range(start, end, days_offset, invert=False)

    @staticmethod
    def to_timestamp(arg, tz=None):
        if isinstance(arg, pd.Timestamp):
            if tz:
                return arg.tz_localize(tz)
            else:
                return arg

        if hasattr(arg, 'to_timestamp'):
            return arg.to_timestamp(tz=tz)

        raise ValueError("Invalid timestamp type")

    def _weeks_in_range(self, start, end, n, invert):
        if not 0 <= n < MAX_WEEK_RANGE:
            raise _out_of_range_error(MAX_WEEK_RANGE)
        if invert:
            days_offset = -n - 1
        else:
            days_offset = n

        week_ends = self._periods('week', days_offset)
        tz = week_ends.index.tz
        idx_start = week_ends.index.searchsorted(self.to_timestamp(start, tz=tz))
        idx_end = week_ends.index.searchsorted(self.to_timestamp(end, tz=tz))
        return pd.DatetimeIndex(week_ends[idx_start: idx_end + 1])

    # @preprocess(start=coerce_string(pd.Period), end=coerce_string(pd.Period))
    def week_ends_in_range(self, start, end, days_offset=0):
        return self._weeks_in_range(start, end, days_offset, invert=True)

    # @preprocess(start=coerce_string(pd.Period), end=coerce_string(pd.Period))
    def week_starts_in_range(self, start, end, days_offset=0):
        return self._weeks_in_range(start, end, days_offset, invert=False)

    def _quarters_in_range(self, start, end, n, invert):
        if not 0 <= n < MAX_QUARTER_RANGE:
            raise _out_of_range_error(MAX_QUARTER_RANGE)
        if invert:
            days_offset = -n - 1
        else:
            days_offset = n

        quarter_ends = self._periods('quarter', days_offset)
        tz = quarter_ends.index.tz
        idx_start = quarter_ends.index.searchsorted(self.to_timestamp(start, tz=tz))
        idx_end = quarter_ends.index.searchsorted(self.to_timestamp(end, tz=tz))
        return pd.DatetimeIndex(quarter_ends[idx_start: idx_end + 1])

    # @preprocess(start=coerce_string_to_quarter_period(), end=coerce_string_to_quarter_period())
    def quarter_ends_in_range(self, start, end, days_offset=0):
        return self._quarters_in_range(start, end, days_offset, invert=True)

    # @preprocess(start=coerce_string_to_quarter_period(), end=coerce_string_to_quarter_period())
    def quarter_starts_in_range(self, start, end, days_offset=0):
        return self._quarters_in_range(start, end, days_offset, invert=False)

    def valid_session_or_next(self, dt):
        idx = self.all_sessions.searchsorted(dt)
        return self.all_sessions[idx]

    def valid_session_or_previous(self, dt):
        idx = self.all_sessions.searchsorted(dt)
        if dt in self.all_sessions:
            return self.all_sessions[idx]

        return self.all_sessions[idx - 1]

    # </editor-fold>


start_default = pd.Timestamp('1970-01-01', tz='UTC')


class GenericExchangeCalendar(ExtendedExchangeCalendar):

    def __init__(self, name, tz=None, open_times=None, close_times=None,
                 break_start_times=None, break_end_times=None,
                 holidays=None, start=start_default, end=None):
        self._name = name

        if not tz:
            tz = timezone('UTC')

        if open_times is None:
            open_times = [(None, time(10, 1))]

        if close_times is None:
            close_times = [(None, time(15, 0))]

        self._open_times = open_times
        self._close_times = close_times
        self._break_start_times = break_start_times
        self._break_end_times = break_end_times

        self._tz = tz

        if holidays is None:
            holidays = []

        self.holidays = holidays

        super().__init__(start, end)

    @property
    def name(self):
        return self._name

    @property
    def tz(self):
        return self._tz

    @property
    def open_times(self):
        return self._open_times

    @property
    def close_times(self):
        return self._close_times

    @property
    def break_start_times(self):
        return self._break_start_times

    @property
    def break_end_times(self):
        return self._break_end_times

    @property
    def adhoc_holidays(self):
        return self.holidays
