name_of_actor = input()
starting_points = float(input())
numb_raters = int(input())

for _ in range(numb_raters):
    diff_actor = input()
    given_points = float(input())
    starting_points = starting_points + ((len(diff_actor) * given_points) / 2)

    if starting_points > 1250.5:
        print(f"Congratulations, {name_of_actor} got a nominee "
              f"for leading role with {starting_points:.1f}!")
        break
else:
    print(f"Sorry, {name_of_actor} you need {1250.5 - starting_points:.1f} more!")
