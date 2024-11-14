puzzle = 2.60
talking_doll = 3
plush_bear = 4.10
minion = 8.20
truck = 2

excursion_price = float(input())
numb_puzzles = int(input())
numb_talking_dolls = int(input())
numb_plush_bear = int(input())
numb_minion = int(input())
numb_trucks = int(input())

price = puzzle * numb_puzzles + talking_doll * numb_talking_dolls + plush_bear * \
        numb_plush_bear + minion * numb_minion + truck * numb_trucks

toys_number = numb_puzzles + numb_talking_dolls + numb_plush_bear + \
              numb_minion + numb_trucks

discount = 0

if toys_number >= 50:
    discount = price * 0.25

final_price = price - discount

rent = final_price * 0.1


win_sum = final_price - rent


money_left = win_sum - excursion_price
money_needed = excursion_price - win_sum

if win_sum >= excursion_price:
    print(f"Yes! {money_left:.2f} lv left.")

if win_sum < excursion_price:
    print(f"Not enough money! {money_needed:.2f} lv needed.")
