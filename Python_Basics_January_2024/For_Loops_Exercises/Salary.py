n = int(input())
salary = int(input())

for _ in range(n):
    command = input()
    if command == 'Facebook':
        salary = salary - 150
    elif command == 'Instagram':
        salary = salary - 100
    elif command == 'Reddit':
        salary = salary - 50

if salary > 0:
    print(salary)
else:
    print('You have lost your salary.')
