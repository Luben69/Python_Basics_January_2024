first_number = int(input())
second_number = int(input())

for num in range(first_number, second_number + 1):

    num_str = str(num)

    odd_sum = 0
    even_sum = 0

    for i in range(6):
        digit = int(num_str[i])

        if i % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit

    if odd_sum == even_sum:
        print(num, end=' ')
