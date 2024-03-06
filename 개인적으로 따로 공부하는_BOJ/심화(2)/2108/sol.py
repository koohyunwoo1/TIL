import sys
sys.stdin = open('input.txt')

N = int(input())
number = []
for n in range(N):
    num = int(input())
    number.append(num)
    number.sort()


print(sum(number) // N)
print(number[N // 2])
print(max(number) - min(number))