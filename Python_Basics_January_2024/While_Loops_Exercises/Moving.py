width = int(input())
length = int(input())
height = int(input())
free_space = width * length * height
all_added = 0
ready = False

while free_space >= 0:
    command = input()

    if command == 'Done':
        ready = True
        break

    added = int(command)
    all_added += added
    free_space -= added

if ready:
    print(f'{free_space} Cubic meters left.')
else:
    print(f'No more free space! You need {abs(free_space)} Cubic meters more.')
