time_per_mile_sec = int(input("Enter time per mile in seconds: "))
pace_minutes = int(time_per_mile_sec // 60)
pace_seconds = int(time_per_mile_sec % 60)
print(f"Average pace per mile: {pace_minutes} minutes {pace_seconds} seconds")
total_hours = time_per_mile_sec / 3600
mile = 1
speed_mph = mile / total_hours
print(f"Average speed is: {speed_mph:.2f} mph")