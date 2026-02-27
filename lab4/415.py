from datetime import datetime, timedelta

def parse_date(line):
    date_part, tz_part = line.strip().split()
    
    year, month, day = map(int, date_part.split("-"))
    
    sign = 1 if "+" in tz_part else -1
    hh, mm = map(int, tz_part[3:].split(":"))
    
    # создаём локальную полночь
    dt = datetime(year, month, day, 0, 0, 0)
    
    # переводим в UTC вручную
    offset = timedelta(hours=hh, minutes=mm) * sign
    dt_utc = dt - offset
    
    return dt_utc

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

birth_line = input()
current_line = input()

birth_dt = parse_date(birth_line)
current_dt = parse_date(current_line)

birth_month = birth_dt.month
birth_day = birth_dt.day

year = current_dt.year

def make_birthday(year):
    m = birth_month
    d = birth_day
    
    if m == 2 and d == 29 and not is_leap(year):
        d = 28
        
    return datetime(year, m, d)

candidate = make_birthday(year)

if candidate < current_dt:
    candidate = make_birthday(year + 1)

diff_seconds = (candidate - current_dt).total_seconds()

print(int(diff_seconds // 86400))