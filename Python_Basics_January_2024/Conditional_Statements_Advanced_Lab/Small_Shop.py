product = input()
city = input()
quantity = float(input())

if product == 'coffee':
    if city == 'Sofia':
        print(0.50 * quantity)
    elif city == 'Plovdiv':
        print(0.40 * quantity)
    elif city == 'Varna':
        print(0.45 * quantity)
elif product == 'water':
    if city == 'Sofia':
        print(0.80 * quantity)
    elif city == 'Plovdiv':
        print(0.70 * quantity)
    elif city == 'Varna':
        print(0.70 * quantity)
elif product == 'beer':
    if city == 'Sofia':
        print(1.20 * quantity)
    elif city == 'Plovdiv':
        print(1.15 * quantity)
    elif city == 'Varna':
        print(1.10 * quantity)
elif product == 'sweets':
    if city == 'Sofia':
        print(1.45 * quantity)
    elif city == 'Plovdiv':
        print(1.30 * quantity)
    elif city == 'Varna':
        print(1.35 * quantity)
elif product == 'peanuts':
    if city == 'Sofia':
        print(1.60 * quantity)
    elif city == 'Plovdiv':
        print(1.50 * quantity)
    elif city == 'Varna':
        print(1.55 * quantity)
