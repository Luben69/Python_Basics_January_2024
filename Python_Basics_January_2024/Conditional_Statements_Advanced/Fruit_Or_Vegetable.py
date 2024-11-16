product = input()
fruit = {'banana', 'apple', 'kiwi', 'cherry', 'lemon', 'grapes'}
veg = {"tomato", "cucumber", "pepper", "carrot"}

if product in fruit:
    print('fruit')
elif product in veg:
    print('vegetable')
else:
    print('unknown')
