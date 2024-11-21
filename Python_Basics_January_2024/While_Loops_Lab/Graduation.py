name = input()
all_grade = 0
current_class = 1
failed = 0

while current_class <= 12:
    new_grade = float(input())

    if new_grade < 4.00:
        failed += 1
        if failed > 1:
            print(f'{name} has been excluded at {current_class} grade')
            break
    else:
        all_grade += new_grade
        current_class += 1

if current_class > 12:
    print(f'{name} graduated. Average grade: {all_grade / 12:.2f}')
