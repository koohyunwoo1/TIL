arr = [0]*10

print(arr)
print(*arr)


# 배열 활용 예제 : Gravity
'''
9
7 4 2 0 0 6 0 7 0
'''
N = int(input())
arr = list(map(int, input().split()))

max_v = 0
for i in range(N-1):
    cnt = 0
    for j in range(i+1, N):
        if arr[i]>arr[j]:
            cnt += 1
    if max_v < cnt: # 최대 낙차보다 크면
        max_v = cnt
print(max_v)


# 버블 정렬
# 2개 이상의 자료를 특정 기준에 의해 작은값부터 또는 반대의 순서대로 재배열하는것

N = 6
arr = [7, 2, 5, 3, 1, 4]


def asc(arr, N):
    for i in range(N-1, 0 ,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

asc(arr, N)
print(arr)

def dec(arr, N):
    for i in range(N-1, 0 ,-1):
        for j in range(i):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


dec(arr, N)
print(arr)


# # 20240130


num = 456789
c = [0] * 12

for i in range(6):
    c[num % 10] += 1
    num // 10


# input() 함수 사용시 문자열로 들어온다.
















