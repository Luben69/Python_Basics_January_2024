from math import floor
pages = int(input())
pages_per_hour = int(input())
days_needed_to_read = int(input())

hours_needed = pages // pages_per_hour
needed_hours_per_day = hours_needed / days_needed_to_read

print(floor(needed_hours_per_day))