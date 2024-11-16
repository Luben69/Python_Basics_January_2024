my_list = []

while True:
    command = input()
    if command == 'Stop':
        print(min(my_list))
        break
    else:
        my_list.append(int(command))
