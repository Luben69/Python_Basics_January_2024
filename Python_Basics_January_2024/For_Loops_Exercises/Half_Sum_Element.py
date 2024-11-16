n = int(input())
my_list = []
biggest = []

for _ in range(n):
    number = int(input())
    my_list.append(number)

element_to_move = max(my_list)

if element_to_move in my_list:
    biggest.append(element_to_move)
    my_list.remove(element_to_move)

if sum(my_list) == element_to_move:
    print(f'Yes\nSum = {element_to_move}')
else:
    print(f'No\nDiff = {abs(sum(my_list)- element_to_move)}')
