start_hours = 6
start_minutes = 52
start_time_sec = (start_hours * 3600) + (start_minutes * 60)
easy_pace_sec = (8 * 60) + 15
tempo_pace_sec = (7 * 60) + 12
total_run_sec = (2 * easy_pace_sec) + (3 * tempo_pace_sec)
arrival_time_sec = start_time_sec + total_run_sec
arrival_hours = arrival_time_sec // 3600
remaining_sec = arrival_time_sec % 3600
arrival_minutes = remaining_sec // 60
arrival_seconds = remaining_sec % 60
print(f"I will get home for breakfast at {arrival_hours}:{arrival_minutes:02d}:{arrival_seconds:02d} AM")