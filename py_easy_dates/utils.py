import re

DAYS = [
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday",
    "mon",
    "tue",
    "wed",
    "thu",
    "fri",
    "sat",
    "sun",
]

MONTHS = {
    "january": "01",
    "february": "02",
    "march": "03",
    "april": "04",
    "june": "06",
    "july": "07",
    "august": "08",
    "september": "09",
    "october": "10",
    "november": "11",
    "december": "12",
    "jan": "01",
    "feb": "02",
    "mar": "03",
    "apr": "04",
    "may": "05",
    "jun": "06",
    "jul": "07",
    "aug": "08",
    "sep": "09",
    "oct": "10",
    "nov": "11",
    "dec": "12",
}


def strip_day(dt_string: str) -> str:
    """Removes day from date string"""

    for day in DAYS:
        res = re.findall(day, dt_string)
        if len(res) > 0:
            dt_string = dt_string.replace(day, "")
            break

    return dt_string


def clean_date(dt_string: str) -> str:
    """Removes ordinals from date"""

    z = re.search(r"\d{1}(st|rd|nd|th)", dt_string)
    if z:
        dt_string = re.sub(z.group(), (z.group()[0]).zfill(2).ljust(3), dt_string)
    dt_string = re.sub(r"[\/\.\s,-]", " ", dt_string)
    dt_string = " ".join(dt_string.split())
    dt_string = dt_string.lower()

    return dt_string


def strip_month(dt_string: str) -> str:
    """Converts months in string to its value in number"""

    for i in MONTHS.keys():
        res = re.findall(i, dt_string)
        if len(res) > 0:
            dt_string = dt_string.replace(i, "{0: ^4}".format(MONTHS[res[0]]))
            break

    return dt_string
