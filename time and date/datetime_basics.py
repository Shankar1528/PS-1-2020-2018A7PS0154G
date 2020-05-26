# curr_date_time.py

from datetime import datetime

curr_datetime = datetime.now()
curr_date = curr_datetime.date()
curr_time = curr_datetime.time()

print(f"The current date time is {curr_datetime}")
print(f"Today's date is {curr_date}")
print(f"Current time is {curr_time}")

curr_year = curr_datetime.year
curr_month = curr_datetime.month
curr_day = curr_datetime.day

curr_hour = curr_datetime.hour
curr_min = curr_datetime.minute
curr_sec = curr_datetime.second

print(f"The current date time is {curr_datetime}")

print(f"The year is {curr_year}")
print(f"The month is {curr_month}")
print(f"The day is {curr_day}")

print(f"Current hour of the day is {curr_hour}")
print(f"Current minute of the day is {curr_min}")
print(f"Current seconds are {curr_sec}")
