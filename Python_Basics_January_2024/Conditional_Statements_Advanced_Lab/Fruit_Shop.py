fruit = input()
day = input()
quantity = float(input())
working_days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"}
not_working_days = {"Saturday", "Sunday"}

if day in working_days:
    if fruit == 'banana':
        print(f"{2.50 * quantity:.2f}")
    elif fruit == 'apple':
        print(f"{1.20 * quantity:.2f}")
    elif fruit == 'orange':
        print(f"{0.85 * quantity:.2f}")
    elif fruit == 'grapefruit':
        print(f"{1.45 * quantity:.2f}")
    elif fruit == 'kiwi':
        print(f"{2.70 * quantity:.2f}")
    elif fruit == 'pineapple':
        print(f"{5.50 * quantity:.2f}")
    elif fruit == 'grapes':
        print(f"{3.85 * quantity:.2f}")
    else:
        print('error')
elif day in not_working_days:
    if fruit == 'banana':
        print(f"{2.70 * quantity:.2f}")
    elif fruit == 'apple':
        print(f"{1.25 * quantity:.2f}")
    elif fruit == 'orange':
        print(f"{0.90 * quantity:.2f}")
    elif fruit == 'grapefruit':
        print(f"{1.60 * quantity:.2f}")
    elif fruit == 'kiwi':
        print(f"{3.00 * quantity:.2f}")
    elif fruit == 'pineapple':
        print(f"{5.60 * quantity:.2f}")
    elif fruit == 'grapes':
        print(f"{4.20 * quantity:.2f}")
    else:
        print('error')
else:
    print('error')
