# PyEasyDates

This code contains a set of functions to make parsing of dates easier.
Instead of specifying the exact format of dates contained in a string, the user can just specify the order of date, month, and year in the date. There are three separate functions available as of now, as listed below.

## dmy()
Parse dates in the order of date, month, and year. It doesn't matter how they are written, whether in words or number, and with what separators, if the date can be read by a human, this function should be able to parse it.
This means that dates like 1012019 will fail to parse as it is not clear whether it is 1st January or 10th January.

## mdy()
Parse dates in the order of month, date, and year. It doesn't matter how they are written, whether in words or number, and with what separators, if the date can be read by a human, this function should be able to parse it.
This means that dates like 1012019 will fail to parse as it is not clear whether it is 1st January or 10th January.

## ymd()
_yet to be added_

Parse dates in the order of year, month, and date. It doesn't matter how they are written, whether in words or number, and with what separators, if the date can be read by a human, this function should be able to parse it.
This means that dates like 2019101 will fail to parse as it is not clear whether it is 1st January or 10th January.

***
## Additional advantages
* Using these functions also provides the additional advantage of not having to run loops for lists. These functions can handle both single element as well as a list.
* The lists also do not have to contain all dates in the exact same format, as long as they follow the same order. This makes it highly advantageous for parsing dates from within a block of text by combining it with regular expressions.

## Upcoming
Time parsing along with dates. For example:
dmy_hms(), 
mdy_hms(),
ymd_hms()
