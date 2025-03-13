from datetime import datetime, timedelta

date_str = input("Enter date (YYYY-MM-DD): ")
dt = datetime.strptime(date_str, "%Y-%m-%d")

# 1 task - subtract 5 days
print("Date 5 days ago:", (dt - timedelta(days=5)).date())

# 2 task - yesterday, today, tomorrow
print("Yesterday:", (dt - timedelta(days=1)).date())
print("Today:", dt.date())
print("Tomorrow:", (dt + timedelta(days=1)).date())

# 3 task - drop microseconds
print("Datetime without microseconds:", dt.replace(microsecond=0))

# 4 task - difference in seconds between two dates
dt1_str = input("Enter first date (YYYY-MM-DD HH:MM:SS): ")
dt2_str = input("Enter second date (YYYY-MM-DD HH:MM:SS): ")
dt1 = datetime.strptime(dt1_str, "%Y-%m-%d %H:%M:%S")
dt2 = datetime.strptime(dt2_str, "%Y-%m-%d %H:%M:%S")
print("Difference in seconds:", (dt2 - dt1).total_seconds())