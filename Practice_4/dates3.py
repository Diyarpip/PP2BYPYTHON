from datetime import datetime


current_datetime = datetime.now()
print(f"With microseconds: {current_datetime}")


datetime_without_microseconds = current_datetime.replace(microsecond=0)
print(f"Without microseconds (replace): {datetime_without_microseconds}")


formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(f"Without microseconds (strftime): {formatted_datetime}")