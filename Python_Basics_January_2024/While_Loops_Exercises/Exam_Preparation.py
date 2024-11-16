max_bad_grades_count = int(input())
all_round_grade = 0
last_problem = ''
count_of_problems = 0
failed = True
times_failed = 0

while times_failed < max_bad_grades_count:

    name_of_problem = input()

    if name_of_problem == 'Enough':
        failed = False
        break

    grade = int(input())

    if grade <= 4:
        times_failed += 1

    count_of_problems += 1
    all_round_grade += grade
    last_problem = name_of_problem

if failed:
    print(f'You need a break, {max_bad_grades_count} poor grades.')
else:
    print(f'Average score: {all_round_grade / count_of_problems:.2f}')
    print(f'Number of problems: {count_of_problems}')
    print(f'Last problem: {last_problem}')
