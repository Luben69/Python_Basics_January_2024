length = int(input())
width = int(input())
pieces = length * width
all_taken_pieces = 0
stopped = False

while pieces > 0:
    command = input()
    if command == 'STOP':
        stopped = True
        break

    taken_pieces = int(command)
    all_taken_pieces += taken_pieces
    pieces = pieces - taken_pieces

if stopped:
    print(f'{pieces} pieces are left.')
else:
    print(f'No more cake left! You need {abs(pieces)} pieces more.')
