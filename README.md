# PyEasyDates

PyEasyDates is a package with the sole goal of making date parsing easier. instead of typing long strftime statements, use intuitive 3/7 character function names to parse dates.

PyEasyDates allows you to use separate functions for specific formats, thereby doing away with the need for specifying formats. The functions are intuitively named, so there's no learning process.
This library makes date handling beginner friendly.

Functions also work with both a single string as well as a list of strings. They will return either a single datetime object, or a list of datetime objects depending on the input.


## List of functions

### dmy()
Parse dates in the order of date, month, and year.

### mdy()
Parse dates in the order of month, date, and year.

### ymd()
Parse dates in the order of year, month, and date.

## Features
* PyEasyDates recognises 2-digit and 4-digit years. 2-digit year is parsed as being between 1931-2030
* PyEasyDates doesn't care about how a month is written, Dec, Decemeber, 12 will all work
* Additional information in date string like ordinals and day names are automatically ignored