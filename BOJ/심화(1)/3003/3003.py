import sys
sys.stdin = open('input.txt')

# 킹 퀸 룩 비숍 나이트 폰

num = list(map(int, input().split()))

ches = [1,1,2,2,2,8]

for i in range(6):
    result = ches[i] - num[i]
    print(result, end = ' ')
