import sys
sys.stdin = open('input.txt')

N = int(input())

result = []

for i in range(1, N+1):
    lst = [N, i]
    while True:
        num = lst[-2] - lst[-1]
        if num >= 0:
            lst.append(num)
        else:
            break
    if len(lst) > len(result):
        result = lst

print(len(result))
for i in result:
    print(i, end=' ')