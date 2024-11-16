wanted_book = input()
count = 0
found = False

while True:
    new_book = input()

    if new_book == wanted_book:
        print(f'You checked {count} books and found it.')
        found = True
        break
    elif new_book == 'No More Books':
        break
    else:
        count += 1

if not found:
    print('The book you search is not here!')
    print(f'You checked {count} books.')
