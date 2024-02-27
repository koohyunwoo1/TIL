# a = [1, 2, 3, 4]
# b = a

# b[0] = 100

# print(a)
# print(b)

a = 100
b = a

b = 9

print(a)  # ??
print(b)  # 9

# 할당
original_list = [1, 2, 3]
copy_list = original_list

copy_list[0] = 'hello'
print(original_list)

# 얕은 복사
a = [1, 2, 3]
b = a[:]

b[0] = 100
print(a)

# 얕은 복사의 한계
a = [1, 2, [100, 200]]
b = a[:]

b[2][0] = 999
print(a)  # ??


import copy

origin_list = [1, 2, [1, 2]]
deep_copy_list = copy.deepcopy(origin_list)

deep_copy_list[2][0] = 999
print(origin_list)
