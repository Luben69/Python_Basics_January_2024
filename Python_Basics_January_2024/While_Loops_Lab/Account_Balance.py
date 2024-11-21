command = input()
money_in_bank = 0
while command != 'NoMoreMoney':
    if float(command) > 0:
        money_in_bank += float(command)
        print(f'Increase: {float(command):.2f}')
    else:
        print('Invalid operation!')
        break
    command = input()
print(f'Total: {money_in_bank:.2f}')
