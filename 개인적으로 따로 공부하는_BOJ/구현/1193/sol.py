import sys
sys.stdin = open('input.txt')

num = int(input())
line = 1

while num > line:
    num -= line
    line += 1
    
if line % 2 == 0:
    a = num
    b = line - num + 1

elif line % 2 == 1:
    a = line - num + 1
    b = num

print(f'{a}/{b}')