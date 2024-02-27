import sys
sys.stdin = open('input.txt')

'''
상근이가 가지고 있으면 1을 아니면 0을 출력해라
시간 초과 뜸......
'''

N = int(input())
N_number = list(map(int, input().split()))    # 상근이가 가지고 있는 카드숫자
M = int(input())
M_number = list(map(int, input().split()))   # 체크해봐야될 숫자카드

cnt = {}

for i in range(N):
    cnt[N_number[i]] = 0


for j in range(M):
    if M_number[j] not in cnt:
        print(0, end=' ')
    else:
        print(1, end=' ')

















# N = int(input())
# N_number = list(map(int, input().split()))
# M = int(input())
# M_number = list(map(int, input().split()))
#
# a = []
# b = []
# result = []
# for i in range(N):
#     a.append(N_number[i])
# for j in range(M):
#     b.append(M_number[j])
#     if b[j] in a:
#         result.append(1)
#     else:
#         result.append(0)
#
# print(*result)


