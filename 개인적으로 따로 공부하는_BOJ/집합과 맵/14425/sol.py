import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())

a = []
b = []

for _ in range(N):
    S = input().rstrip()  # 문자열 끝의 개행문자를 제거합니다.
    a.append(S)
    print(S)
for _ in range(M):
    check = input().rstrip()  # 문자열 끝의 개행문자를 제거합니다.
    b.append(check)

result = 0
for check in b:
    if check in a:
        result += 1

print(result)
