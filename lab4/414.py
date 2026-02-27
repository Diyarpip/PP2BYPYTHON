from datetime import datetime, timedelta
import re

def parse_datetime(s):
    # Формат: "YYYY-MM-DD UTC±HH:MM"
    match = re.match(r'(\d{4})-(\d{2})-(\d{2}) UTC([+-])(\d{2}):(\d{2})', s)
    if not match:
        raise ValueError("Invalid format")
    year, month, day, sign, hour, minute = match.groups()
    year, month, day = int(year), int(month), int(day)
    hour, minute = int(hour), int(minute)
    
    # Создаем datetime в местную полночь
    dt_local = datetime(year, month, day, 0, 0, 0)
    
    # Смещение в секундах
    offset_seconds = hour * 3600 + minute * 60
    if sign == '+':
        # UTC = местное - смещение
        dt_utc = dt_local - timedelta(seconds=offset_seconds)
    else:
        # UTC = местное + смещение
        dt_utc = dt_local + timedelta(seconds=offset_seconds)
    
    return dt_utc

def main():
    s1 = input().strip()
    s2 = input().strip()
    
    dt1_utc = parse_datetime(s1)
    dt2_utc = parse_datetime(s2)
    
    diff_seconds = abs((dt2_utc - dt1_utc).total_seconds())
    days = int(diff_seconds // 86400)
    
    print(days)

if __name__ == "__main__":
    main()