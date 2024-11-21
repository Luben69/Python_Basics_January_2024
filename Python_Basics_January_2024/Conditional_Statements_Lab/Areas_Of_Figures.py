from math import pi
figure = input()

if figure == "square":
    numb1 = float(input())
    face = numb1 * numb1
    print(face)

elif figure == "rectangle":
    numb1 = float(input())
    numb2 = float(input())
    face = numb1 * numb2
    print(face)

elif figure == "circle":
    numb1 = float(input())
    face = pi * (numb1 ** 2)
    print(face)

elif figure == "triangle":
    numb1 = float(input())
    numb2 = float(input())
    face = (numb1 / 1/2) * numb2
    print(face)
