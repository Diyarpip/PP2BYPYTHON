from datetime import datetime, timedelta


current_date = datetime.now().date()


five_days_ago = current_date - timedelta(days=5)

print(f"Current date: {current_date}")
print(f"Date five days ago: {five_days_ago}")