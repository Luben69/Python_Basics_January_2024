n = int(input())
all_grades = []
count = 0

while True:
    individual_grade = 0
    presentation = input()

    if presentation == "Finish":
        break
    count += 1

    for _ in range(n):
        grade = float(input())
        individual_grade += grade

    individual_grade /= n
    all_grades.append(individual_grade)

    print(f"{presentation} - {individual_grade:.2f}.")

print(f"Student's final assessment is {sum(all_grades) / count:.2f}.")
