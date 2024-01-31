# 20240131

# 배열 2(arr 2)
# 2차원 배열

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# 1차원 배열 만들때
arr2 = [0] * N
# 2차원 배열 만들때
arr3 = [[0] * N for _ in range(N)]
arr3[0][0] = 1   # 2차원 배열 arr3의 첫번째 리스트 첫번째 값을 1로 바꿔줌.
print(arr3)

# 배열 순회
# n X m 배열의 모든 원소를 빠짐없이 조사하는 방법

# 행 우선 순회
n, m  = 3, 4                               
for i in range(n): # 0 1 2               0
    for j in range(m): # 0 1 2 3         1
        f'(array[i][j])'     #           2

# 열 우선 순회
for j in range(m):
    for i in range(n):
        f'(array[j][i]'

# 지그재그 순회
# 홀수형의 역 방향
for i in range(n):
    for j in range(m):
        f'(array[i][j + (m-1-2*j)*(i%2)])'
        # 고정된 값에서 증가하는 값 빼주기

# 짝수형의 역 방향
for i in range(n):
    for j in range(m):
        f'(array[i][j + (m-1-2*j)*((i+1)%2)])'


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

i = 3
j = 4
for k in range(4):
    ni = i + di[k]
    nj = j + dj[k]
    print(ni, nj)

# 행 25 열 4

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


N = 5
for i in range(N):    # 행
    for j in range(N):     # 열
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            print((ni, nj), end = ' ')
        print()


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N = 5
arr = [[0] * N for _ in range(N)]
for i in range(N):  # 행  0 1 2 3 4
    for j in range(N):  # 열   0 1 2 3 4
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                print(arr[ni][nj], end=' ')
        print()


# 전치 행렬
arr = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(3):   # 행   0 1 2
    for j in range(3):     # 열 0 1 2
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i] , arr[i][j]



# 부분 집합
bit = [0,0,0,0]
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                


# 부분집합
arr = [1,2,3]
subsets = [[]]

for num in arr:
    size = len(subsets)
    for y in range(size):
        subsets.append(subsets[y]+[num])
print(subsets)



# 연습문제, 부분집합의 합
'''
10
-7 -5 2 3 8 -2 4 6 9
'''
N = 100
arr = list(map(int, '-7 -5 2 3 8 -2 4 6 9 0'.split()))
arr = list(range(1, 101))
# 부분집합의 합이 55미만인 경우만 모은 리스트

# print(arr)
# print(2**10)
# print(1 << N)
# print(bin(1024))


for i in range(1, 1<<N):
    lst = []
    print(i, '번째 경우의 수')
    for j in range(N):
        # print(1 << j)
        # i번째 경우의 수에, j번째 요소가 포함 되어 있는 부분집합인지 확인하는 코드
        # i번째가 3번째라면 ->  0b 0011
        # j번째 요소(0번째 1 .....) -> 0b 0001, 0010 , 0011
        if i & (1 << j):
            lst.append(arr[j])
            if sum(lst) >= 55:
                break
    if sum(lst) < 55:
        print(lst)
        # print('있음')
        # break
    print(lst)

