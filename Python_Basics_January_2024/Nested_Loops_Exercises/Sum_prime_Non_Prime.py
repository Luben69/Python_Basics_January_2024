sum_prime = 0
sum_non_prime = 0

while True:
    cmd = input()
    if cmd == "stop":
        break

    cmd = int(cmd)

    if cmd < 0:
        print("Number is negative.")
        continue
    if cmd <= 1:
        sum_non_prime += cmd
        continue

    # Check if the number is prime
    is_prime = True
    for i in range(2, int(cmd ** 0.5) + 1):
        if cmd % i == 0:
            is_prime = False
            break

    if is_prime:
        sum_prime += cmd
    else:
        sum_non_prime += cmd

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")
