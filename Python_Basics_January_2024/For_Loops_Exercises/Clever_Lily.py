age = int(input())
washing_machine = float(input())
price_toys = int(input())
numb_toys = 0
coins = 10
wallet = 0

for year in range(1, age + 1):
    if year % 2 == 0:
        wallet += coins - 1
        coins += 10
    else:
        numb_toys += 1

wallet += numb_toys * price_toys

if wallet >= washing_machine:
    print(f'Yes! {wallet - washing_machine:.2f}')
else:
    print(f'No! {washing_machine - wallet:.2f}')
