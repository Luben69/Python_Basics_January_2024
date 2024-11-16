while True:
    destination = input()

    if destination == 'End':
        break

    min_budget = float(input())

    all_saved_money = 0

    while all_saved_money < min_budget:
        amount = float(input())
        all_saved_money += amount

    print(f'Going to {destination}!')
