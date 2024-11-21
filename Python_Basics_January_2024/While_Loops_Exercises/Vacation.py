money_needed = float(input())
in_pocket_money = float(input())
days_spending_in_a_row = 0
all_days = 0

while in_pocket_money < money_needed and days_spending_in_a_row < 5:

    action = input()
    new = float(input())
    all_days += 1

    if action == 'spend':
        in_pocket_money -= new
        days_spending_in_a_row += 1
        if in_pocket_money < 0:
            in_pocket_money = 0
    elif action == 'save':
        in_pocket_money += new
        days_spending_in_a_row = 0

if in_pocket_money >= money_needed:
    print(f'You saved the money for {all_days} days.')

if days_spending_in_a_row == 5:
    print(f"You can't save the money.")
    print(all_days)
