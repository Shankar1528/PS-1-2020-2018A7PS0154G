
from datetime import datetime,timedelta

# Get the base date and time
base_date_time = datetime.now()
print(base_date_time)

# Format it to January 1, 1970
print(datetime.strftime(base_date_time, "%B %d, %Y"))

# Print the day of the week with time in AM/PM
print(datetime.strftime(base_date_time, "%A, %I:%M:%S %p"))


time_diff = timedelta(weeks=-1,
                    days=-3)

# Subtract time diff to the current time
req_date_time = base_date_time + time_diff

print(req_date_time)
