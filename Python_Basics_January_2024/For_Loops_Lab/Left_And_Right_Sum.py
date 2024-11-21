n = int(input())
my_list = []

for _ in range(2 * n):
    number = int(input())
    my_list.append(number)

left_sum = sum(my_list[:n])

right_sum = sum(my_list[n:])

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    diff = abs(left_sum - right_sum)
    print(f"No, diff = {diff}")
