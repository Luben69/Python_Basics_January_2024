exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_time = exam_hour * 60 + exam_minute
arrival_time = arrival_hour * 60 + arrival_minute

difference = arrival_time - exam_time

if difference > 0:
    print("Late")
    if difference == 60:
        print(f"1:00 hours after the start")
    elif difference < 60:
        print(f"{difference} minutes after the start")
    else:
        hours = difference // 60
        minutes = difference % 60
        print(f"{hours}:{minutes:02d} hours after the start")
elif difference >= -30:
    print("On time")
    if difference < 0:
        print(f"{-difference} minutes before the start")
elif difference >= -60:
    print("Early")
    if -difference == 60:
        print(f"1:00 hours before the start")
    else:
        print(f"{-difference} minutes before the start")
else:
    print("Early")
    hours = -difference // 60
    minutes = -difference % 60
    if hours == 1 and minutes == 0:
        print(f"1:00 hours before the start")
    else:
        print(f"{hours}:{minutes:02d} hours before the start")
