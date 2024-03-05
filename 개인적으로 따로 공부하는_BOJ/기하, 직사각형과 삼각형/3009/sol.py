import sys
sys.stdin = open('input.txt')

a = []
b = []

for i in range(3):
    N, M = map(int, input().split())
    a.append(N)
    b.append(M)

for i in range(3):
    if a.count(a[i]) == 1:
        a4 = a[i]
    if b.count(b[i]) == 1:
        b4 = b[i]

print(a4, b4)
