import datetime
import warnings
from typing import Callable, List, Literal, Sequence, Union

from .utils import clean_date, strip_day, strip_month


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

    day_pos: int = format.index("d")
    month_pos: int = format.index("m")
    year_pos: int = format.index("y")

    if len(date_string) == 8:
        year: str = date_string[year_pos * 2 : year_pos * 2 + 4]  # noqa
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

    def func(dates: Union[str, list]) -> Union[datetime.datetime, List[datetime.datetime]]:
        if isinstance(dates, str):
            dates = parse_date(dates, format)
        elif isinstance(dates, Sequence):
            dates = [parse_date(i, format) for i in dates]
        else:
            raise TypeError(f"Type not recognised '{dates.__class__.__name__}'")
        return dates

    return func


dmy: Callable = create_func("dmy")
mdy: Callable = create_func("mdy")
ymd: Callable = create_func("ymd")
