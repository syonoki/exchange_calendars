"""
Last update: 2018-10-26
"""

from exchange_calendars.extensions.calendar_extension import ExtendedExchangeCalendar
from pandas import (
    Timestamp,
)
from pandas.tseries.holiday import (
    Holiday,
    previous_friday,
)
from exchange_calendars.exchange_calendar import HolidayCalendar

from datetime import time
from itertools import chain
from pytz import timezone

KRNewYearsDay = Holiday(
    'New Years Day',
    month=1,
    day=1)

KRIndependenceDay = Holiday(
    'Independence Day',
    month=3,
    day=1
)

KRArbourDay = Holiday(
    'Arbour Day',
    month=4,
    day=5,
    end_date=Timestamp('2006-01-01'),
)

KRLabourDay = Holiday(
    'Labour Day',
    month=5,
    day=1
)

KRChildrensDay = Holiday(
    'Labour Day',
    month=5,
    day=5
)

# 현충일
KRMemorialDay = Holiday(
    'Memorial Day',
    month=6,
    day=6
)

# 제헌절
KRConstitutionDay = Holiday(
    'Constitution Day',
    month=7,
    day=17,
    end_date=Timestamp('2008-01-01')
)

# 광복절
KRLiberationDay = Holiday(
    'Liberation Day',
    month=8,
    day=15
)

# 개천절
KRNationalFoundationDay = Holiday(
    'NationalFoundationDay',
    month=10,
    day=3
)

Christmas = Holiday(
    'Christmas',
    month=12,
    day=25
)

# 한글날
KRHangulProclamationDay = Holiday(
    'Hangul Proclamation Day',
    month=10,
    day=9,
    start_date=Timestamp('2013-01-01')
)

# KRX 연말 휴장
KRXEndOfYearClosing = Holiday(
    'KRX Year-end Closing',
    month=12,
    day=31,
    observance=previous_friday,
    start_date=Timestamp('2001-01-01')
)

KRXEndOfYearClosing2000 = [
    Timestamp('2000-12-27', tz='UTC'),
    Timestamp('2000-12-28', tz='UTC'),
    Timestamp('2000-12-29', tz='UTC'),
    Timestamp('2000-12-30', tz='UTC'),
]

# Lunar New Year
KRLunarNewYear = [
    # 2000
    Timestamp('2000-02-04', tz='UTC'),
    # 2001
    Timestamp('2001-01-23', tz='UTC'),
    Timestamp('2001-01-24', tz='UTC'),
    Timestamp('2001-01-25', tz='UTC'),
    # 2002
    Timestamp('2002-02-11', tz='UTC'),
    Timestamp('2002-02-12', tz='UTC'),
    Timestamp('2002-02-13', tz='UTC'),
    # 2003
    Timestamp('2003-01-31', tz='UTC'),
    # 2004
    Timestamp('2004-01-21', tz='UTC'),
    Timestamp('2004-01-22', tz='UTC'),
    Timestamp('2004-01-23', tz='UTC'),

    # 2005
    Timestamp('2005-02-08', tz='UTC'),
    Timestamp('2005-02-09', tz='UTC'),
    Timestamp('2005-02-10', tz='UTC'),

    # 2006
    Timestamp('2006-01-28', tz='UTC'),
    Timestamp('2006-01-29', tz='UTC'),
    Timestamp('2006-01-30', tz='UTC'),

    # 2007
    Timestamp('2007-02-19', tz='UTC'),

    # 2008
    Timestamp('2008-02-06', tz='UTC'),
    Timestamp('2008-02-07', tz='UTC'),
    Timestamp('2008-02-08', tz='UTC'),

    # 2009
    Timestamp('2009-01-25', tz='UTC'),
    Timestamp('2009-01-26', tz='UTC'),
    Timestamp('2009-01-27', tz='UTC'),

    # 2010
    Timestamp('2010-02-13', tz='UTC'),
    Timestamp('2010-02-14', tz='UTC'),
    Timestamp('2010-02-15', tz='UTC'),

    # 2011
    Timestamp('2011-02-02', tz='UTC'),
    Timestamp('2011-02-03', tz='UTC'),
    Timestamp('2011-02-04', tz='UTC'),

    # 2012
    Timestamp('2012-01-23', tz='UTC'),
    Timestamp('2012-01-24', tz='UTC'),

    # 2013
    Timestamp('2013-02-11', tz='UTC'),

    # 2014
    Timestamp('2014-01-30', tz='UTC'),
    Timestamp('2014-01-31', tz='UTC'),

    # 2015
    Timestamp('2015-02-18', tz='UTC'),
    Timestamp('2015-02-19', tz='UTC'),
    Timestamp('2015-02-20', tz='UTC'),

    # 2016
    Timestamp('2016-02-07', tz='UTC'),
    Timestamp('2016-02-08', tz='UTC'),
    Timestamp('2016-02-09', tz='UTC'),
    Timestamp('2016-02-10', tz='UTC'),

    # 2017
    Timestamp('2017-01-27', tz='UTC'),
    Timestamp('2017-01-28', tz='UTC'),
    Timestamp('2017-01-29', tz='UTC'),
    Timestamp('2017-01-30', tz='UTC'),

    # 2018
    Timestamp('2018-02-15', tz='UTC'),
    Timestamp('2018-02-16', tz='UTC'),
    Timestamp('2018-02-17', tz='UTC'),

    # 2019
    Timestamp('2019-02-04', tz='UTC'),
    Timestamp('2019-02-05', tz='UTC'),
    Timestamp('2019-02-06', tz='UTC'),

    # 2020
    Timestamp('2020-01-24', tz='UTC'),
    Timestamp('2020-01-25', tz='UTC'),
    Timestamp('2020-01-26', tz='UTC'),
    Timestamp('2020-01-27', tz='UTC'),

    # 2021
    Timestamp('2021-02-11', tz='UTC'),
    Timestamp('2021-02-12', tz='UTC'),

    # 2022
    Timestamp('2022-01-31', tz='UTC'),
    Timestamp('2022-02-01', tz='UTC'),
    Timestamp('2022-02-02', tz='UTC'),

    # 2023
    Timestamp('2023-01-23', tz='UTC'),
    Timestamp('2023-01-24', tz='UTC'),
]

# Election Days
KRElectionDays = [
    Timestamp('2000-04-13', tz='UTC'),  # National Assembly
    Timestamp('2002-06-13', tz='UTC'),  # Regional election
    Timestamp('2002-12-19', tz='UTC'),  # Presidency
    Timestamp('2004-04-15', tz='UTC'),  # National Assembly
    Timestamp('2006-05-31', tz='UTC'),  # Regional election
    Timestamp('2007-12-19', tz='UTC'),  # Presidency
    Timestamp('2008-04-09', tz='UTC'),  # National Assembly
    Timestamp('2010-06-02', tz='UTC'),  # Local election
    Timestamp('2012-04-11', tz='UTC'),  # National Assembly
    Timestamp('2012-12-19', tz='UTC'),  # Presidency
    Timestamp('2014-06-04', tz='UTC'),  # Local election
    Timestamp('2016-04-13', tz='UTC'),  # National Assembly
    Timestamp('2017-05-09', tz='UTC'),  # Presidency
    Timestamp('2018-06-13', tz='UTC'),  # Local election
    Timestamp('2020-04-15', tz='UTC'),  # National Assembly
    Timestamp('2022-03-09', tz='UTC'),  # Presidency
    Timestamp('2022-06-01', tz='UTC'),  # Local election
]

# Buddha's birthday
KRBuddhasBirthday = [
    Timestamp('2000-05-11', tz='UTC'),
    Timestamp('2001-05-01', tz='UTC'),
    Timestamp('2003-05-08', tz='UTC'),
    Timestamp('2004-05-26', tz='UTC'),
    Timestamp('2005-05-15', tz='UTC'),
    Timestamp('2006-05-05', tz='UTC'),
    Timestamp('2007-05-24', tz='UTC'),
    Timestamp('2008-05-12', tz='UTC'),
    Timestamp('2009-05-02', tz='UTC'),
    Timestamp('2010-05-21', tz='UTC'),
    Timestamp('2011-05-10', tz='UTC'),
    Timestamp('2012-05-28', tz='UTC'),
    Timestamp('2013-05-17', tz='UTC'),
    Timestamp('2014-05-06', tz='UTC'),
    Timestamp('2015-05-25', tz='UTC'),
    Timestamp('2016-05-14', tz='UTC'),
    Timestamp('2017-05-03', tz='UTC'),
    Timestamp('2018-05-22', tz='UTC'),
    Timestamp('2020-04-30', tz='UTC'),
    Timestamp('2021-05-19', tz='UTC'),
]

# Harvest Moon Day
KRHarvestMoonDay = [
    # 2000
    Timestamp('2000-09-11', tz='UTC'),
    Timestamp('2000-09-12', tz='UTC'),
    Timestamp('2000-09-13', tz='UTC'),
    # 2001
    Timestamp('2001-10-01', tz='UTC'),
    Timestamp('2001-10-02', tz='UTC'),
    # 2002
    Timestamp('2002-09-20', tz='UTC'),
    # 2003
    Timestamp('2003-09-10', tz='UTC'),
    Timestamp('2003-09-11', tz='UTC'),
    Timestamp('2003-09-12', tz='UTC'),
    # 2004
    Timestamp('2004-09-27', tz='UTC'),
    Timestamp('2004-09-28', tz='UTC'),
    Timestamp('2004-09-29', tz='UTC'),
    # 2005
    Timestamp('2005-09-17', tz='UTC'),
    Timestamp('2005-09-18', tz='UTC'),
    Timestamp('2005-09-19', tz='UTC'),
    # 2006
    Timestamp('2006-10-05', tz='UTC'),
    Timestamp('2006-10-06', tz='UTC'),
    Timestamp('2006-10-07', tz='UTC'),
    # 2007
    Timestamp('2007-09-24', tz='UTC'),
    Timestamp('2007-09-25', tz='UTC'),
    Timestamp('2007-09-26', tz='UTC'),
    # 2008
    Timestamp('2008-09-13', tz='UTC'),
    Timestamp('2008-09-14', tz='UTC'),
    Timestamp('2008-09-15', tz='UTC'),
    # 2009
    Timestamp('2009-10-02', tz='UTC'),
    Timestamp('2009-10-03', tz='UTC'),
    Timestamp('2009-10-04', tz='UTC'),
    # 2010
    Timestamp('2010-09-21', tz='UTC'),
    Timestamp('2010-09-22', tz='UTC'),
    Timestamp('2010-09-23', tz='UTC'),
    # 2011
    Timestamp('2011-09-12', tz='UTC'),
    Timestamp('2011-09-13', tz='UTC'),
    # 2012
    Timestamp('2012-10-01', tz='UTC'),
    # 2013
    Timestamp('2013-09-18', tz='UTC'),
    Timestamp('2013-09-19', tz='UTC'),
    Timestamp('2013-09-20', tz='UTC'),
    # 2014
    Timestamp('2014-09-08', tz='UTC'),
    Timestamp('2014-09-09', tz='UTC'),
    Timestamp('2014-09-10', tz='UTC'),
    # 2015
    Timestamp('2015-09-28', tz='UTC'),
    Timestamp('2015-09-29', tz='UTC'),
    # 2016
    Timestamp('2016-09-14', tz='UTC'),
    Timestamp('2016-09-15', tz='UTC'),
    Timestamp('2016-09-16', tz='UTC'),
    # 2017
    Timestamp('2017-10-03', tz='UTC'),
    Timestamp('2017-10-04', tz='UTC'),
    Timestamp('2017-10-05', tz='UTC'),
    Timestamp('2017-10-06', tz='UTC'),
    # 2018
    Timestamp('2018-09-23', tz='UTC'),
    Timestamp('2018-09-24', tz='UTC'),
    Timestamp('2018-09-25', tz='UTC'),
    Timestamp('2018-09-26', tz='UTC'),
    # 2019
    Timestamp('2019-09-12', tz='UTC'),
    Timestamp('2019-09-13', tz='UTC'),
    # 2020
    Timestamp('2020-09-30', tz='UTC'),
    Timestamp('2020-10-01', tz='UTC'),
    Timestamp('2020-10-02', tz='UTC'),
    # 2021
    Timestamp('2021-09-20', tz='UTC'),
    Timestamp('2021-09-21', tz='UTC'),
    Timestamp('2021-09-22', tz='UTC'),
    # 2022
    Timestamp('2022-09-09', tz='UTC'),
    Timestamp('2022-09-12', tz='UTC'),  # 대체휴일
    # 2023
    Timestamp('2023-09-28', tz='UTC'),
    Timestamp('2023-09-29', tz='UTC'),
    Timestamp('2023-10-02', tz='UTC'), # 임시공휴일
]

# 대체휴일
KRSubstitutionHolidayForChildrensDay2018 = [
    Timestamp('2018-05-07', tz='UTC')
]

# 임시공휴일
KRCelebrationForWorldCupHosting = [
    Timestamp('2002-07-01', tz='UTC')
]

KRSeventyYearsFromIndependenceDay = [
    Timestamp('2015-08-14', tz='UTC')
]

KRTemporaryHolidayForChildrensDay2016 = [
    Timestamp('2016-05-06', tz='UTC')
]

KRTemporaryHolidayForHarvestMoonDay2017 = [
    Timestamp('2017-10-02', tz='UTC')
]

KRTemporaryHolidayForChildrenDay2018 = [
    Timestamp('2018-05-07', tz='UTC')
]

KRTemporaryHolidayForChildrenDay2019 = [
    Timestamp('2019-05-06', tz='UTC')
]

KRTemporaryHolidayForLiberationDay2020 = [
    Timestamp('2020-08-17', tz='UTC')
]
KRTemporaryHoliday2021 = [
    Timestamp('2021-08-16', tz='UTC'),  # 광복절 대체휴일
    Timestamp('2021-10-04', tz='UTC'),  # 개천절 대체휴일
    Timestamp('2021-10-11', tz='UTC'),  # 한글날 대체휴일
]

KRTemporaryHoliday2022 = [
    Timestamp('2022-10-10', tz='UTC'),  # 한글날 대체휴일
]

KRTemporaryHoliday2023 = [
    Timestamp('2023-05-29', tz='UTC'),  # 부처님 오신날 대체휴일
]

# 잘 모르겠는 휴장일
HolidaysNeedToCheck = [
    Timestamp('2000-01-03', tz='UTC')
]

HolidaysBefore1999 = [
    Timestamp('1990-01-01', tz='UTC'),
    Timestamp('1990-01-02', tz='UTC'),
    Timestamp('1990-01-03', tz='UTC'),
    Timestamp('1990-01-29', tz='UTC'),
    Timestamp('1990-03-01', tz='UTC'),
    Timestamp('1990-04-05', tz='UTC'),
    Timestamp('1990-05-02', tz='UTC'),
    Timestamp('1990-06-06', tz='UTC'),
    Timestamp('1990-07-17', tz='UTC'),
    Timestamp('1990-08-15', tz='UTC'),
    Timestamp('1990-09-03', tz='UTC'),
    Timestamp('1990-10-01', tz='UTC'),
    Timestamp('1990-10-03', tz='UTC'),
    Timestamp('1990-10-09', tz='UTC'),
    Timestamp('1990-12-25', tz='UTC'),
    Timestamp('1991-01-01', tz='UTC'),
    Timestamp('1991-01-02', tz='UTC'),
    Timestamp('1991-02-14', tz='UTC'),
    Timestamp('1991-02-15', tz='UTC'),
    Timestamp('1991-03-01', tz='UTC'),
    Timestamp('1991-04-05', tz='UTC'),
    Timestamp('1991-05-21', tz='UTC'),
    Timestamp('1991-06-06', tz='UTC'),
    Timestamp('1991-07-17', tz='UTC'),
    Timestamp('1991-08-15', tz='UTC'),
    Timestamp('1991-09-23', tz='UTC'),
    Timestamp('1991-10-03', tz='UTC'),
    Timestamp('1991-12-25', tz='UTC'),
    Timestamp('1991-12-30', tz='UTC'),
    Timestamp('1992-01-01', tz='UTC'),
    Timestamp('1992-09-10', tz='UTC'),
    Timestamp('1992-09-11', tz='UTC'),
    Timestamp('1992-10-03', tz='UTC'),
    Timestamp('1992-12-25', tz='UTC'),
    Timestamp('1992-12-29', tz='UTC'),
    Timestamp('1992-12-30', tz='UTC'),
    Timestamp('1992-12-31', tz='UTC'),
    Timestamp('1993-01-01', tz='UTC'),
    Timestamp('1993-01-22', tz='UTC'),
    Timestamp('1993-03-01', tz='UTC'),
    Timestamp('1993-04-05', tz='UTC'),
    Timestamp('1993-05-05', tz='UTC'),
    Timestamp('1993-05-28', tz='UTC'),
    Timestamp('1993-07-17', tz='UTC'),
    Timestamp('1993-09-29', tz='UTC'),
    Timestamp('1993-09-30', tz='UTC'),
    Timestamp('1993-10-01', tz='UTC'),
    Timestamp('1993-12-29', tz='UTC'),
    Timestamp('1993-12-30', tz='UTC'),
    Timestamp('1993-12-31', tz='UTC'),
    Timestamp('1994-01-02', tz='UTC'),
    Timestamp('1994-02-09', tz='UTC'),
    Timestamp('1994-02-10', tz='UTC'),
    Timestamp('1994-02-11', tz='UTC'),
    Timestamp('1994-03-01', tz='UTC'),
    Timestamp('1994-04-05', tz='UTC'),
    Timestamp('1994-05-05', tz='UTC'),
    Timestamp('1994-06-06', tz='UTC'),
    Timestamp('1994-07-17', tz='UTC'),
    Timestamp('1994-08-15', tz='UTC'),
    Timestamp('1994-09-19', tz='UTC'),
    Timestamp('1994-09-20', tz='UTC'),
    Timestamp('1994-09-21', tz='UTC'),
    Timestamp('1994-10-03', tz='UTC'),
    Timestamp('1994-12-29', tz='UTC'),
    Timestamp('1994-12-30', tz='UTC'),
    Timestamp('1995-01-02', tz='UTC'),
    Timestamp('1995-01-30', tz='UTC'),
    Timestamp('1995-01-31', tz='UTC'),
    Timestamp('1995-02-01', tz='UTC'),
    Timestamp('1995-03-01', tz='UTC'),
    Timestamp('1995-05-01', tz='UTC'),
    Timestamp('1995-05-05', tz='UTC'),
    Timestamp('1995-06-06', tz='UTC'),
    Timestamp('1995-06-27', tz='UTC'),
    Timestamp('1995-07-17', tz='UTC'),
    Timestamp('1995-08-15', tz='UTC'),
    Timestamp('1995-09-08', tz='UTC'),
    Timestamp('1995-09-09', tz='UTC'),
    Timestamp('1995-10-03', tz='UTC'),
    Timestamp('1995-12-22', tz='UTC'),
    Timestamp('1995-12-25', tz='UTC'),
    Timestamp('1995-12-28', tz='UTC'),
    Timestamp('1995-12-29', tz='UTC'),
    Timestamp('1995-12-30', tz='UTC'),
    Timestamp('1995-12-31', tz='UTC'),
    Timestamp('1996-01-01', tz='UTC'),
    Timestamp('1996-01-02', tz='UTC'),
    Timestamp('1996-02-19', tz='UTC'),
    Timestamp('1996-02-20', tz='UTC'),
    Timestamp('1996-03-01', tz='UTC'),
    Timestamp('1996-04-05', tz='UTC'),
    Timestamp('1996-04-11', tz='UTC'),
    Timestamp('1996-05-01', tz='UTC'),
    Timestamp('1996-05-05', tz='UTC'),
    Timestamp('1996-05-24', tz='UTC'),
    Timestamp('1996-06-06', tz='UTC'),
    Timestamp('1996-07-17', tz='UTC'),
    Timestamp('1996-08-15', tz='UTC'),
    Timestamp('1996-09-26', tz='UTC'),
    Timestamp('1996-09-27', tz='UTC'),
    Timestamp('1996-09-28', tz='UTC'),
    Timestamp('1996-10-03', tz='UTC'),
    Timestamp('1996-12-25', tz='UTC'),
    Timestamp('1996-12-30', tz='UTC'),
    Timestamp('1996-12-31', tz='UTC'),
    Timestamp('1997-01-01', tz='UTC'),
    Timestamp('1997-01-02', tz='UTC'),
    Timestamp('1997-02-07', tz='UTC'),
    Timestamp('1997-02-08', tz='UTC'),
    Timestamp('1997-03-01', tz='UTC'),
    Timestamp('1997-04-05', tz='UTC'),
    Timestamp('1997-05-05', tz='UTC'),
    Timestamp('1997-05-14', tz='UTC'),
    Timestamp('1997-06-06', tz='UTC'),
    Timestamp('1997-07-17', tz='UTC'),
    Timestamp('1997-08-15', tz='UTC'),
    Timestamp('1997-09-16', tz='UTC'),
    Timestamp('1997-09-17', tz='UTC'),
    Timestamp('1997-10-03', tz='UTC'),
    Timestamp('1997-12-25', tz='UTC'),
    Timestamp('1998-01-01', tz='UTC'),
    Timestamp('1998-01-02', tz='UTC'),
    Timestamp('1998-01-27', tz='UTC'),
    Timestamp('1998-01-28', tz='UTC'),
    Timestamp('1998-01-29', tz='UTC'),
    Timestamp('1998-03-01', tz='UTC'),
    Timestamp('1998-04-05', tz='UTC'),
    Timestamp('1998-05-01', tz='UTC'),
    Timestamp('1998-05-03', tz='UTC'),
    Timestamp('1998-05-05', tz='UTC'),
    Timestamp('1998-06-04', tz='UTC'),
    Timestamp('1998-06-06', tz='UTC'),
    Timestamp('1998-07-17', tz='UTC'),
    Timestamp('1998-08-15', tz='UTC'),
    Timestamp('1998-10-03', tz='UTC'),
    Timestamp('1998-10-04', tz='UTC'),
    Timestamp('1998-10-05', tz='UTC'),
    Timestamp('1998-10-06', tz='UTC'),
    Timestamp('1998-12-25', tz='UTC'),
    Timestamp('1998-12-31', tz='UTC'),
    Timestamp('1999-01-01', tz='UTC'),
    Timestamp('1999-02-15', tz='UTC'),
    Timestamp('1999-02-16', tz='UTC'),
    Timestamp('1999-02-17', tz='UTC'),
    Timestamp('1999-03-01', tz='UTC'),
    Timestamp('1999-04-05', tz='UTC'),
    Timestamp('1999-05-05', tz='UTC'),
    Timestamp('1999-05-22', tz='UTC'),
    Timestamp('1999-06-06', tz='UTC'),
    Timestamp('1999-07-17', tz='UTC'),
    Timestamp('1999-09-23', tz='UTC'),
    Timestamp('1999-09-24', tz='UTC'),
    Timestamp('1999-09-25', tz='UTC'),
    Timestamp('1999-10-03', tz='UTC'),
    Timestamp('1999-12-29', tz='UTC'),
    Timestamp('1999-12-30', tz='UTC'),
    Timestamp('1999-12-31', tz='UTC'),
]


class KRXExchangeCalendar(ExtendedExchangeCalendar):
    """
    Exchange calendars for KRX

    Open Time: 9:00 AM, Asia/Seoul
    Close Time: 3:30 PM, Asia/Seoul (3:00 PM until 2016/07/31)

    """

    @property
    def name(self):
        return "KRX"

    @property
    def tz(self):
        # return timezone('Asia/Seoul')
        return timezone('UTC')

    @property
    def open_time(self):
        return time(9, 0)

    @property
    def open_times(self):
        return [(None, time(9, 0))]

    @property
    def close_time(self):
        return time(15, 30)

    @property
    def close_times(self):
        return [(None, time(15, 30))]

    @property
    def regular_holidays(self):
        return HolidayCalendar([
            KRNewYearsDay,
            KRIndependenceDay,
            KRArbourDay,
            KRLabourDay,
            KRChildrensDay,
            KRMemorialDay,
            KRConstitutionDay,
            KRLiberationDay,
            KRNationalFoundationDay,
            Christmas,
            KRHangulProclamationDay,
            KRXEndOfYearClosing
        ])

    @property
    def special_closes(self):
        return []

    @property
    def adhoc_holidays(self):
        return list(chain(
            KRXEndOfYearClosing2000,
            KRLunarNewYear,
            KRElectionDays,
            KRBuddhasBirthday,
            KRHarvestMoonDay,
            KRSubstitutionHolidayForChildrensDay2018,
            KRCelebrationForWorldCupHosting,
            KRSeventyYearsFromIndependenceDay,
            KRTemporaryHolidayForChildrensDay2016,
            KRTemporaryHolidayForHarvestMoonDay2017,
            KRTemporaryHolidayForChildrenDay2018,
            KRTemporaryHolidayForChildrenDay2019,
            HolidaysNeedToCheck,
            KRTemporaryHolidayForLiberationDay2020,
            KRTemporaryHoliday2021,
            KRTemporaryHoliday2022,
            KRTemporaryHoliday2023,
            HolidaysBefore1999,
        ))

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.__class__ == other.__class__
