import re
from datetime import datetime
import warnings

def strip_day(dt_string):
    my_days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", 
               "mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    for i in my_days:
        res = re.findall(i, dt_string)
        if len(res) > 0:
            dt_string = dt_string.replace(i, "")
            break
    return(dt_string)

def clean_date(dt_string):
    z = re.match(r"\d{1}(st|rd|nd|th)", dt_string)
    if z: dt_string = re.sub(z.group(), (z.group()[0]).zfill(2).ljust(3), dt_string)
    dt_string = re.sub(r"[\/\.\s,-]", " ", dt_string)
    dt_string = " ".join(dt_string.split())
    dt_string = dt_string.lower()
    return(dt_string)
    
def strip_month(dt_string):
    month_vals = {"january":"01", "february":"02", "march":"03", "april":"04", "june":"06", "july":"07", 
                  "august":"08", "september":"09", "october":"10", "november":"11", "december":"12", 
                  "jan":"01", "feb":"02", "mar":"03", "apr":"04", "may":"05", "jun":"06", 
                  "jul":"07", "aug":"08", "sep":"09", "oct":"10", "nov":"11", "dec":"12"}
    for i in month_vals.keys():
        res = re.findall(i, dt_string)
        if len(res) > 0:
            dt_string = dt_string.replace(i, '{0: ^4}'.format(month_vals[res[0]]))
            break
    return(dt_string)
    
def parse_dmy(dt_string):
    dt_string = strip_day(clean_date(dt_string))
    dt_string = strip_month(clean_date(dt_string))
    dat = dt_string.split()
    if len(dat) == 1:
        if (len(dt_string) == 8 or len(dt_string) == 6):
            dat = [dt_string[0:2], dt_string[2:4], dt_string[4:len(dt_string)]]
        else:
            raise Exception("Failed to parse as DMY")
    if(len(dat[0]) == 1): dat[0] = str(dat[0]).zfill(2)
    if(int(dat[0])>31):
        raise Exception('Day value out of range: {}'.format(dat[0]))
    if(len(dat[1]) == 1): dat[1] = str(dat[1]).zfill(2)
    if(int(dat[1])>12):
        raise Exception('Month value out of range: {}'.format(dat[1]))
    if(len(dat[2])==2):
        warnings.warn("2-digit year found in {}, parsing in the year range 1931-2030".format("-".join(dat)))
        dat[2] = ("20" if int(dat[2])<31 else "19") + dat[2]
    dat = datetime.strptime("-".join(dat), "%d-%m-%Y")
    return(dat)

def dmy(dt_string):
    if type(dt_string) == str:
        dates = parse_dmy(dt_string)
    else:
        dates = [parse_dmy(i) for i in dt_string]
    return(dates)
