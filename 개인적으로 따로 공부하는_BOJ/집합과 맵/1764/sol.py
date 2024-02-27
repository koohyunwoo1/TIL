import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())

a = []
b = []


for i in range(N):
    listen = input()
    a.append(listen)
for j in range(M):
    see = input()
    b.append(see)

result = sorted(list(set(a) & set(b)))
print(len(result))
for i in result:
    print(i)


