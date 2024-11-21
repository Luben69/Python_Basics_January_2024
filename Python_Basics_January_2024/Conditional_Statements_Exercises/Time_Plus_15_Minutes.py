hours = int(input())
minutes = int(input())

c_minutes_15 = minutes + 15

if c_minutes_15 >= 60:
    c_minutes_15 = c_minutes_15 - 60
    hours = hours + 1

if hours >= 24:
    hours = 0

print(f"{hours}:{c_minutes_15:02d}")
