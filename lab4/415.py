from datetime import datetime, timedelta, timezone
import math

def parse_line(line):
    date_part, tz_part = line.split()
    year, month, day = map(int, date_part.split('-'))
    
    sign = 1 if '+' in tz_part else -1
    hh, mm = map(int, tz_part[4:].split(':'))
    offset = timezone(sign * timedelta(hours=hh, minutes=mm))
    
    return year, month, day, offset

def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

birth_line = input()
current_line = input()

by, bm, bd, birth_tz = parse_line(birth_line)
cy, cm, cd, current_tz = parse_line(current_line)

current_dt = datetime(cy, cm, cd, 0, 0, 0, tzinfo=current_tz).astimezone(timezone.utc)

def make_birthday(year):
    day = bd
    if bm == 2 and bd == 29 and not is_leap(year):
        day = 28
    return datetime(year, bm, day, 0, 0, 0, tzinfo=birth_tz).astimezone(timezone.utc)

next_birthday = make_birthday(cy)

if next_birthday < current_dt:
    next_birthday = make_birthday(cy + 1)

seconds = (next_birthday - current_dt).total_seconds()

days = math.ceil(seconds / 86400)

print(days)