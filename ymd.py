from datetime import datetime
import warnings
import re
from EasyDateSupportFunctions import strip_day, strip_month, clean_date
    
def parse_ymd(dt_string):
    dt_string = strip_day(clean_date(dt_string))
    dt_string = strip_month(clean_date(dt_string))
    dat = dt_string.split()
    if len(dat) == 1:
        if (len(dt_string) == 6):
            dat = [dt_string[0:2], dt_string[2:4], dt_string[4:6]]
        elif (len(dt_string) == 8):
            dat = [dt_string[0:4], dt_string[4:6], dt_string[6:8]]
        else:
            raise Exception("Failed to parse as YMD")
    if(len(dat[1]) == 1): dat[1] = str(dat[1]).zfill(2)
    if(int(dat[1])>12):
        raise Exception('Month value out of range: {}'.format(dat[1]))
    if(len(dat[2]) == 1): dat[2] = str(dat[2]).zfill(2)
    if(int(dat[2])>31):
        raise Exception('Day value out of range: {}'.format(dat[2]))
    if(len(dat[0])==2):
        warnings.warn("2-digit year found in {}, parsing in the year range 1931-2030".format("-".join(dat)))
        dat[0] = ("20" if int(dat[0])<31 else "19") + dat[0]
    dat = datetime.strptime("-".join(dat), "%Y-%m-%d")
    return(dat)

def ymd(dt_string):
    if type(dt_string) == str:
        dates = parse_ymd(dt_string)
    elif type(dt_string) == dict:
        dt_string = list(dt_string.values())
        dates = [parse_ymd(i) for i in dt_string]
    elif type(dt_string) == list:
        dates = [parse_ymd(i) for i in dt_string]
    else:
        raise Exception("Unsupported data type, only string, list, and dict are supported. Nested dict or list will result in an error.")
    return(dates)
