import datetime
import warnings
from typing import Literal

from utils import clean_date, strip_day, strip_month


def parse_date(date_string: str, format: Literal["dmy", "mdy", "ymd"]) -> datetime.datetime:
    """Parses dates based on format

    parameters:
    -----------
    date_string: str
        Date-like string.
        Can contain both 4-digit and 2-digit years.

    format: dmy | mdy | ymd
        Defines the order of day, month, and year in the date.
        parser is separator agnostic.
        parser will also convert month names to month numbers, remove day names and ordinals.

    Returns:
    --------
        Returns a datetime.datetime object
    """

    date_string = strip_day(clean_date(date_string))
    date_string = strip_month(clean_date(date_string)).replace(" ", "")

    day_pos = format.index("d")
    month_pos = format.index("m")
    year_pos = format.index("y")

    if len(date_string) == 8:
        year = date_string[year_pos * 2 : year_pos * 2 + 4]  # noqa
        date_string = date_string.replace(year, "aa")

    if len(date_string) == 6:
        date_string: list = [date_string[i : i + 2] for i in range(0, 6, 2)]  # noqa

    day = int(date_string[day_pos])
    month = int(date_string[month_pos])

    if date_string[year_pos] != "aa":
        year = int(date_string[year_pos])
        warnings.warn("Two-digit year found, parsing between 1931-2030")
        year = 2000 + year if year < 31 else 1900 + year
    else:
        year = int(year)

    return datetime.datetime(year, month, day)


def create_func(format):
    """Helper function to create other functions for each supported format"""

    def func(dt_string):
        if type(dt_string) == str:
            dates = parse_date(dt_string, format)
        else:
            dates = [parse_date(i, format) for i in dt_string]
        return dates

    return func


dmy = create_func("dmy")
mdy = create_func("mdy")
ymd = create_func("ymd")
