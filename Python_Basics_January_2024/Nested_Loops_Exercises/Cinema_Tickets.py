student_all = 0
standard_all = 0
kid_all = 0
all_tickets_sold = 0

while True:
    movie_name = input()
    whole_thing = 0
    student = 0
    standard = 0
    kid = 0
    if movie_name == "Finish":
        break

    free_spaces = int(input())

    for _ in range(free_spaces):
        cmd = input()
        if cmd == "End":
            break
        else:
            if cmd == "student":
                student += 1
                student_all += 1
            elif cmd == "standard":
                standard += 1
                standard_all += 1
            elif cmd == "kid":
                kid += 1
                kid_all += 1
    whole_thing = student + standard + kid
    all_tickets_sold += whole_thing
    print(f"{movie_name} - {(whole_thing / free_spaces) * 100:.2f}% full.")

print(f"Total tickets: {all_tickets_sold}")
print(f"{(student_all / all_tickets_sold) * 100:.2f}% student tickets.")
print(f"{(standard_all / all_tickets_sold) * 100:.2f}% standard tickets.")
print(f"{(kid_all / all_tickets_sold) * 100:.2f}% kids tickets.")
