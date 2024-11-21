count_of_group_climbers = int(input())
all_people = 0
musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0

for _ in range(count_of_group_climbers):
    persons = int(input())
    if 0 < persons <= 5:
        musala += persons
        all_people += persons
    elif 6 <= persons <= 12:
        monblan += persons
        all_people += persons
    elif 13 <= persons <= 25:
        kilimandjaro += persons
        all_people += persons
    elif 26 <= persons <= 40:
        k2 += persons
        all_people += persons
    else:
        everest += persons
        all_people += persons


print(f'{musala / all_people * 100:.2f}%')
print(f'{monblan / all_people * 100:.2f}%')
print(f'{kilimandjaro / all_people * 100:.2f}%')
print(f'{k2 / all_people * 100:.2f}%')
print(f'{everest / all_people * 100:.2f}%')
