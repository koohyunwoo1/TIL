items = ['apple', 'banana', 'coconut']   # 리스트로 되어있음.
for item in items:
    print(item)


country = 'Korea'
for char in country:
    print(char)


for i in range(5):
    print(i)


my_dict = {
    'x': 10,
    'y': 20,
    'z': 30,
}
for key in my_dict:
    print(key)
    print(my_dict[key])


numbers = [4, 6, 10, -8, 5]
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
print(numbers)


outers = ['A', 'B']
inners = ['c', 'd']
for outer in outers:
    for inner in inners:
        print(outer, inner)


elements = [['A', 'B'], ['c', 'd']]
for elem in elements:
    print(elem)
