'''
10
-7 -5 2 3 8 -2 4 6 9
'''
N = 100
# arr = list(map(int,  '-7 -5 2 3 8 -2 4 6 9 0'.split()))
arr = list(range(1, 101))
# 부분집합의 합이 55 미만인 경우만 모은 리스트
# print(arr)
print(2**N)
# print(1 << N)
# print(bin(1024))
# for i in range(1, 1 << N):
#     lst = []
#     print(i, '번째 경우의 수')
#     for j in range(N-1, -1, -1):
#         if i & (1 << j):
#             lst.append(arr[j])
#             if sum(lst) >= 55:  # 부분집합의 합이 55이상이 되면조사 종료
#                 break
#     if sum(lst) < 55:   # 부분집합의 합이 55 미만인 경우만 출력
#         print(lst)
        # print(1 << j)
        # i번째 경우의 수에, j번째 요소가 포함 되어있는 부분집합인지 확인하는코드
        # i번째가 3번째라면 -> 0b 0011
        # j번쨰 요소 (0번쨰, 1번째, 2번째...) -> 0b 0001, 0010, 0011
        # if i & (1 << j):
        #     lst.append(arr[j])
    # if sum(lst) == 0:
    #     print(lst)
    #     print('있어용')
    #     break
    # print(lst)