age = float(input())
sex = input()

if sex == 'm':
    if age < 16:
        print('Master')
    else:
        print('Mr.')
elif sex == 'f':
    if age < 16:
        print('Miss')
    else:
        print('Ms.')
