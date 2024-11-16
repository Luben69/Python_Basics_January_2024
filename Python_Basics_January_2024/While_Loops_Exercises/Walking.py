overall = 0

while overall < 10000:
    command = input()

    if command == 'Going home':
        new = int(input())
        overall += new
        break

    steps = int(command)
    overall += steps

if overall >= 10000:
    print('Goal reached! Good job!')
    print(f'{overall - 10000} steps over the goal!')
else:
    print(f'{10000 - overall} more steps to reach goal.')
