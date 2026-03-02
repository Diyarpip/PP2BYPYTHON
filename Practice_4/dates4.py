from datetime import datetime, timedelta


def date_difference_in_seconds(date1, date2):
    """Calculate difference between two dates in seconds"""
    difference = abs(date2 - date1)
    return difference.total_seconds()


date1 = datetime(2024, 1, 1, 12, 0, 0)  
date2 = datetime(2024, 1, 2, 12, 0, 0)  

seconds_diff = date_difference_in_seconds(date1, date2)
print(f"Date 1: {date1}")
print(f"Date 2: {date2}")
print(f"Difference in seconds: {seconds_diff} seconds")
print(f"Difference in hours: {seconds_diff / 3600} hours")


def get_date_difference_seconds():
    """Get date difference in seconds from user input"""
    try:
        print("\nEnter first date (YYYY-MM-DD HH:MM:SS):")
        date_str1 = input("Date 1: ")
        date1 = datetime.strptime(date_str1, "%Y-%m-%d %H:%M:%S")
        
        print("Enter second date (YYYY-MM-DD HH:MM:SS):")
        date_str2 = input("Date 2: ")
        date2 = datetime.strptime(date_str2, "%Y-%m-%d %H:%M:%S")
        
        difference = date_difference_in_seconds(date1, date2)
        print(f"\nDifference in seconds: {difference} seconds")
        
        
        minutes = difference / 60
        hours = minutes / 60
        days = hours / 24
        
        print(f"Difference in minutes: {minutes:.2f} minutes")
        print(f"Difference in hours: {hours:.2f} hours")
        print(f"Difference in days: {days:.2f} days")
        
        return difference
    except ValueError as e:
        print(f"Error: Invalid date format. {e}")
        return None


current_time = datetime.now()
future_date = current_time + timedelta(days=5, hours=3, minutes=30)

diff_seconds = date_difference_in_seconds(current_time, future_date)
print(f"\nCurrent time: {current_time}")
print(f"Future date: {future_date}")
print(f"Difference in seconds: {diff_seconds} seconds")

