floor_count = int(input())
rooms_count = int(input())
my_list = []

for i in range(floor_count, 0, -1):
    rooms = []

    if floor_count == 1:
        for y in range(0, rooms_count):
            rooms.append(f'L{i}{y}')

    else:
        if i == floor_count:
            for l in range(0, rooms_count):
                rooms.append(f'L{i}{l}')

        else:
            for n in range(0, rooms_count):
                if i % 2 == 1:
                    rooms.append(f'A{i}{n}')
                else:
                    rooms.append(f'O{i}{n}')
    my_list.append(" ".join(rooms))

for char in my_list:
    print(char)