import datetime
import pytz

def get_time_in_timezone(timezone):
    now = datetime.datetime.now(pytz.timezone(timezone))
    return now

def determine_day_or_night(timezone):
    local_time = get_time_in_timezone(timezone)
    hour = local_time.hour
    if 6 <= hour < 18:
        return ""
    else:
        return ""

timezones = ["America/New_York", "Europe/London", "Asia/Tokyo", "Australia/Sydney"]

for timezone in timezones:
    current_time = get_time_in_timezone(timezone)
    day_or_night = determine_day_or_night(timezone)

    print(f"{timezone}: {current_time.strftime('%Y-%m-%d %H:%M:%S')}, {day_or_night}.")
