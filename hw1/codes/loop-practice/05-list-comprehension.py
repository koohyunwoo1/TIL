numbers = [1, 2, 3, 4, 5]
squared_numbers = []

for num in numbers:
    squared_numbers.append(num**2)

print(squared_numbers)  # [1, 4, 9, 16, 25]


# List comprehension
numbers = [1, 2, 3, 4, 5]
squared_numbers = [num**2 for num in numbers]

print(squared_numbers)  # [1, 4, 9, 16, 25]


result = []
for i in range(10):
    if i % 2 == 1:
        result.append(i)

# List comprehension
result = [i for i in range(10) if i % 2 == 1]
