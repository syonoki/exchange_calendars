from datetime import tzinfo
from functools import lru_cache, partial

import pandas as pd
import pytz
from commonutils.input_validation import coerce_string, optional, expect_types
from commonutils.preprocess import preprocess
from commonutils.pydata import mask_dates_between
from commonutils.datetime.date_func import to_timestamp, coerce_string_to_timestamp_with_tz, \
    coerce_tz_aware_timestamp


# TODO: start_date, end_date를 datetime으로 바꿀것인가.


# @lru_cache(maxsize=None)
def get_biz_dates(calendar, start_date=None, end_date=None, with_tz=False):
    biz_days = calendar.all_sessions
    if not with_tz:
        biz_days = biz_days.tz_localize(None)

    mask = mask_dates_between(biz_days, start_date, end_date)
    biz_days = biz_days[mask] if mask is not None else biz_days
    biz_days = pd.DatetimeIndex(biz_days)
    return biz_days


# @lru_cache()
@preprocess(tz=coerce_string(pytz.timezone))
@expect_types(tz=optional(tzinfo))
def previous_biz_date(cal, dt, n=1, tz=None):
    biz_dates = get_biz_dates(cal)

    if dt in biz_dates:
        return biz_dates[biz_dates.get_loc(dt) - n]

    return find_closest_date_before(dt, biz_dates, tz=tz)


# @lru_cache()
@preprocess(tz=coerce_string(pytz.timezone))
@expect_types(tz=optional(tzinfo))
def nth_prev_date(cal, dt, n_period, tz=None):
    biz_dates = get_biz_dates(cal)
    if not dt in biz_dates:
        dt = find_closest_date_before(dt, biz_dates, tz=tz)

    return biz_dates[biz_dates.get_loc(dt) - (n_period - 1)]


@preprocess(tz=coerce_string(pytz.timezone))
@expect_types(tz=optional(tzinfo))
def find_valid_start_end_dates(calendar, start, end, tz=None):
    with_tz = tz is not None
    biz_dates = get_biz_dates(calendar, with_tz=with_tz)
    start_right_shifted = find_closest_date_after(start, biz_dates, tz=tz)
    end_left_shifted = find_closest_date_before(end, biz_dates, tz=tz)

    return start_right_shifted, end_left_shifted


def _apply_tz(date: pd.Timestamp, tz):
    if not date.tz:
        date = date.tz_localize(tz=tz)
    return date


@preprocess(tz=coerce_string(pytz.timezone))
@expect_types(tz=optional(tzinfo))
def find_closest_date_after(start_date, biz_dates, tz=None):
    if start_date in biz_dates:
        target_date = to_timestamp(start_date)
    else:
        after_dates = biz_dates[biz_dates > start_date]
        target_date = after_dates[0]

    return _apply_tz(target_date, tz=tz) if tz is not None else target_date


@preprocess(tz=coerce_string(pytz.timezone))
@expect_types(tz=optional(tzinfo))
def find_closest_date_before(end_date, biz_dates, n=1, tz=None):
    if end_date in biz_dates:
        target_date = to_timestamp(end_date)
    else:
        before_dates = biz_dates[biz_dates < end_date]
        target_date = before_dates[-n]
    return _apply_tz(target_date, tz=tz) if tz is not None else target_date


@preprocess(start=coerce_string_to_timestamp_with_tz(tz='utc'), end=coerce_string_to_timestamp_with_tz(tz='utc'))
@preprocess(start=coerce_tz_aware_timestamp(tz='utc'), end=coerce_tz_aware_timestamp(tz='utc'))
def special_holidays(cal, start='1980-01-01', end='2040-01-01'):
    adhoc_holidays = [h.to_datetime64() for h in cal.adhoc_holidays if (h >= start) and (h <= end)]
    if cal.regular_holidays:
        regular_holidays = cal.regular_holidays.holidays(start=start, end=end)
        ret_val = adhoc_holidays + list(regular_holidays.values)
    else:
        ret_val = adhoc_holidays
    return pd.DatetimeIndex(ret_val).sort_values()


def weekends(start, end):
    all_dates = pd.date_range(start, end)
    basic_bdays = pd.date_range(start, end, freq='B')
    weekends = set(all_dates.values) - set(basic_bdays.values)
    weekends = pd.DatetimeIndex(weekends)
    weekends = weekends.sort_values()

    return weekends


def total_holidays(cal, start, end):
    sh = special_holidays(cal, start, end)
    w_ends = weekends(start, end)

    ret_val = pd.DatetimeIndex(w_ends.append(sh))
    ret_val = ret_val.sort_values()
    return ret_val


def coerce_string_to_quarter_period():
    return coerce_string(
        partial(pd.Period, freq='Q')
    )
