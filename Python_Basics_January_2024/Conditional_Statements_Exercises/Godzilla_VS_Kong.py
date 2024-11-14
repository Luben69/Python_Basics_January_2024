budget = float(input())
walk_on_count = int(input())
clothes_cost_per_walk_on = float(input())

scene_cost = budget * 0.10

if walk_on_count > 150:
    clothes_cost_per_walk_on *= 0.90

total_cost = scene_cost + walk_on_count * clothes_cost_per_walk_on

if total_cost > budget:
    money_needed = total_cost - budget
    print('Not enough money!')
    print(f'Wingard needs {money_needed:.2f} leva more.')
else:
    money_left = budget - total_cost
    print('Action!')
    print(f'Wingard starts filming with {money_left:.2f} leva left.')