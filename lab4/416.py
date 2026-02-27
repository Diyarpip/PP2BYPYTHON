import sys
from datetime import datetime, timezone, timedelta

def parse_date(s):
    # Split the string to separate the date-time part and the UTC offset
    parts = s.split(' UTC')
    dt_str = parts[0]
    offset_str = parts[1]
    
    # Parse the main datetime
    dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
    
    # Parse the offset (e.g., +03:00 or -05:30)
    sign = 1 if offset_str[0] == '+' else -1
    h, m = map(int, offset_str[1:].split(':'))
    
    # Create the timezone object and attach it
    tz = timezone(timedelta(hours=sign * h, minutes=sign * m))
    return dt.replace(tzinfo=tz)

def solve():
    try:
        line1 = sys.stdin.readline().strip()
        line2 = sys.stdin.readline().strip()
        
        if not line1 or not line2:
            return

        start = parse_date(line1)
        end = parse_date(line2)
        
        # Calculating the difference returns a timedelta object
        duration = end - start
        print(int(duration.total_seconds()))
    except EOFError:
        pass

if __name__ == "__main__":
    solve()