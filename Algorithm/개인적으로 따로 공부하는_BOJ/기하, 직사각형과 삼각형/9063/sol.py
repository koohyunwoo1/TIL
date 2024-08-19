import sys
sys.stdin = open('input.txt')

N = int(input())

x_lst = []
y_lst = []

for n in range(N):
    x, y = map(int, input().split())
    x_lst.append(x)
    y_lst.append(y)
    x_lst.sort()
    y_lst.sort()

a = x_lst[N-1] - x_lst[0]
b = y_lst[N-1] - y_lst[0]

print(a * b)