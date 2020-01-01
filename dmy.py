from supportFunctions import strip_day, strip_month, clean_date

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
