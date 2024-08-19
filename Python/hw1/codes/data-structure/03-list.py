my_list = [1, 2, 3]

# append
my_list.append(4)
my_list.append([10, 9, 8])
# print(my_list.append([10, 9, 8]))  # None
print(my_list)

# extend
my_list.extend([4, 5, 6])
print(my_list)

my_list.insert(3, 'ssafy')
print(my_list)

my_list.remove(4)
print(my_list)

item1 = my_list.pop()
print(item1)

item2 = my_list.pop(0)
print(item2)

print(my_list)

index = my_list.index(2)
print(index)

my_list = [1, 3, 2, 2, 3, 3]
count_num = my_list.count(3)
print(count_num)

my_list = [3, 2, 1]
my_list.sort()
print(my_list)

my_list.sort(reverse=True)
print(my_list)

my_list = [1, 3, 2, 8, 1, 9]
my_list.reverse()
print(my_list)
