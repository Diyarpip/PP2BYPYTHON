from datetime import datetime, timedelta
import re

def parse_datetime(s):
    match = re.match(r'(\d{4})-(\d{2})-(\d{2}) UTC([+-])(\d{2}):(\d{2})', s)
    year, month, day, sign, hour, minute = match.groups()
    year, month, day = int(year), int(month), int(day)
    hour, minute = int(hour), int(minute)
    
    offset_seconds = hour * 3600 + minute * 60
    if sign == '+':
        offset_seconds = -offset_seconds  # local ahead of UTC
    return (year, month, day), offset_seconds

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_birthday_utc(birth_year, birth_month, birth_day, offset_seconds, target_year):
    if birth_month == 2 and birth_day == 29 and not is_leap_year(target_year):
        month, day = 2, 28
    else:
        month, day = birth_month, birth_day
    
    dt_local = datetime(target_year, month, day, 0, 0, 0)
    dt_utc = dt_local + timedelta(seconds=offset_seconds)
    return dt_utc

def main():
    s1 = input().strip()
    s2 = input().strip()
    
    (byear, bmonth, bday), boffset = parse_datetime(s1)
    (cyear, cmonth, cday), coffset = parse_datetime(s2)
    
    current_local = datetime(cyear, cmonth, cday, 0, 0, 0)
    current_utc = current_local + timedelta(seconds=coffset)
    
    if (bmonth, bday) > (cmonth, cday):
        target_year = cyear
    else:
        target_year = cyear + 1
    
    birthday_utc = get_birthday_utc(byear, bmonth, bday, boffset, target_year)
    
    diff_seconds = (birthday_utc - current_utc).total_seconds()
    if diff_seconds < 0:
        diff_seconds = 0
    
    days = int(diff_seconds // 86400)
    print(days)

if __name__ == "__main__":
    main()