n = int(input())
my_list = []

for _ in range(n):
    number = int(input())
    my_list.append(number)

even_numbers = sum(my_list[0::2])
odd_numbers = sum(my_list[1::2])

if even_numbers == odd_numbers:
    print(f"Yes \nSum = {even_numbers}")
else:
    print(f"No \nDiff = {abs(even_numbers - odd_numbers)}")
