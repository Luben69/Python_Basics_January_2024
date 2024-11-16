n = int(input())
my_list = []

for _ in range(n):
    number = int(input())
    my_list.append(number)

print(f'Max number: {max(my_list)}')
print(f'Min number: {min(my_list)}')