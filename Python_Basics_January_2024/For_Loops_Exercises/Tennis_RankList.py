from math import floor

numb_of_matches = int(input())
starting_points = int(input())
won_points = 0
w_count = 0


for _ in range(numb_of_matches):
    command = input()
    if command == 'W':
        starting_points += 2000
        won_points += 2000
        w_count += 1
    elif command == 'F':
        starting_points += 1200
        won_points += 1200
    elif command == 'SF':
        starting_points += 720
        won_points += 720

print(f'Final points: {starting_points}')
print(f'Average points: {floor(won_points / numb_of_matches)}')
print(f'{w_count / numb_of_matches * 100:.2f}%')
