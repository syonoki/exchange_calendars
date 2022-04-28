import pytest

from exchange_calendars.exchange_calendar_xmil import XMILExchangeCalendar
from .test_exchange_calendar import ExchangeCalendarTestBase


class TestXMILCalendar(ExchangeCalendarTestBase):
    @pytest.fixture(scope="class")
    def calendar_cls(self):
        yield XMILExchangeCalendar

    @pytest.fixture
    def max_session_hours(self):
        # The XMIL is open from 9:00 am to 5:30 pm.
        yield 8.5

    @pytest.fixture
    def regular_holidays_sample(self):
        yield [
            # 2018
            "2018-01-01",  # New Year's Day
            "2018-03-30",  # Good Friday
            "2018-04-02",  # Easter Monday
            "2018-05-01",  # Labor Day
            "2018-08-15",  # Ferragosto
            "2018-12-24",  # Christmas Eve
            "2018-12-25",  # Christmas Day
            "2018-12-26",  # Boxing Day
            "2018-12-31",  # New Year's Eve
        ]

    @pytest.fixture
    def non_holidays_sample(self):
        yield [
            # Holidays that fall on a weekend and are not made up. Ensure surrounding
            # days are not holidays.
            # In 2017 New Year's Day fell on a Sunday, so the Friday before and
            # the Monday after should both be open.
            "2016-12-30",
            "2017-01-02",
            # In 2015 Ferragosto fell on a Saturday, so the Friday before and
            # the Monday after should both be open.
            "2015-08-14",
            "2015-08-17",
            # In 2010 Labour Day fell on a Saturday, so the market should be
            # open on both the prior Friday and the following Monday.
            "2010-04-30",
            "2010-05-03",
            # Christmas also fell on a Saturday, meaning Boxing Day fell on a
            # Sunday. The market should be closed on Christmas Eve (Friday) but
            # still be open on both the prior Thursday and the next Monday.
            "2010-12-23",
            "2010-12-27",
        ]
