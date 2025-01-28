import sys
input = sys.stdin.readline

N = int(input())
arr1 = [0] * 3    # 후보별 총 점수 배열
arr2 = [0] * 3    # 후보별 선호도 점수를 제곱해서 합산한 배열
for _ in range(N):
    a, b, c = map(int, input().strip().split())
    # 후보마다 점수 더해주기
    arr1[0] += a
    arr1[1] += b
    arr1[2] += c
    # 제곱해서 더해주기
    arr2[0] += a*a
    arr2[1] += b*b
    arr2[2] += c*c
# print(arr1, arr2)

max_value = max(arr1)
if arr1.count(max_value) == 1:	# 총합 가장 큰 사람 1명이면
    for i in range(3):
        if arr1[i] == max_value:
            print(i+1, max_value)
else:	# 그렇지 않다면 
    next_max_value = max(arr2)
    idx = arr2.index(next_max_value)
    if arr2.count(next_max_value) == 1:	  # 제곱합이 가장 큰 사람이 1명이면
        print(idx+1, arr1[idx])
    else:	# 그렇지 않으면 1등 없음
        print(0, arr1[idx])