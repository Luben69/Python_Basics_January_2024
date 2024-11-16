change = float(input())

coins = [2.00, 1.00, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]
count = 0

for coin in coins:
    while change >= coin:
        change -= coin
        change = round(change, 2)
        count += 1

print(count)
