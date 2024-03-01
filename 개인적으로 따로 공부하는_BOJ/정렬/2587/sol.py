import sys
sys.stdin = open('input.txt')

avr = 0
mid = 0

num = []
for i in range(5):
    num.append(int(input()))
num.sort()

print(sum(num) // 5)
print(num[2])