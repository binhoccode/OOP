import time
total_seconds = time.time()
sec_per_minute = 60
sec_per_hour = sec_per_minute * 60
sec_per_day = sec_per_hour * 24
total_days = int(total_seconds // sec_per_day)
seconds_today = total_seconds % sec_per_day
hours = int(seconds_today // sec_per_hour)
minutes = int((seconds_today % sec_per_hour) // sec_per_minute)
seconds = int(seconds_today % sec_per_minute)
print(f"Total days since the epoch: {total_days} days")
print(f"Current time of day (GMT): {hours:02d}:{minutes:02d}:{seconds:02d}")