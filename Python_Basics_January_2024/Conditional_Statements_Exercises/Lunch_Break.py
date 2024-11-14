from math import ceil

series = input()
episode_duration = int(input())
break_duration = int(input())

lunch_time = break_duration * 1 / 8
relax_time = break_duration * 1 / 4

remaining_time = break_duration - (lunch_time + relax_time)

if remaining_time >= episode_duration:
    print(f"You have enough time to watch {series} and left "
          f"with {ceil(remaining_time - episode_duration)} minutes free time.")
else:
    print(f"You don't have enough time to "
          f"watch {series}, you need {ceil(episode_duration - remaining_time)} more minutes.")
