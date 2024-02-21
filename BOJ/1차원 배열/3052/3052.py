import sys
sys.stdin = open('input.txt')


num_list = []

for i in range(10):
    num = int(input())
    num_na = num % 42
    if num_na not in num_list:
        num_list.append(num_na)

print(len(num_list))