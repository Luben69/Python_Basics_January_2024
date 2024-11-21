i = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for _ in range(i):
    numbers = int(input())
    if numbers < 200:
        p1 += 1
    elif 200 <= numbers <= 399:
        p2 += 1
    elif 400 <= numbers <= 599:
        p3 += 1
    elif 600 <= numbers <= 799:
        p4 += 1
    else:
        p5 += 1

print(f'{p1 / i * 100:.2f}%')
print(f'{p2 / i * 100:.2f}%')
print(f'{p3 / i * 100:.2f}%')
print(f'{p4 / i * 100:.2f}%')
print(f'{p5 / i * 100:.2f}%')
