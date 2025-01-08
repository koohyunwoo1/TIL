L = int(input())
N = int(input())
arr = [0 for _ in range(L + 1)]  # L : (1 ≤ L ≤ 1000)
mx = 0  # 가장 많은 조각을 받을 예상 방청객 번호
mx_i = 0
for n in range(N):
    P, K = map(int, input().split())
    if K - P > mx:  # 여러명인 경우 번호가 작은 사람을 출력하도록 초과 범위 지정
        mx_i = n + 1
        mx = K - P
    for i in range(P, K + 1):
        if arr[i] == 0:  # 이미 번호 적혀있으면 받지 못함
            arr[i] = n + 1
print(mx_i)  # 가장 많은 조각을 받을 것으로 기대하고 있던 방청객의 번호를 출력
real = 0
real_i = 0  # 실제로 많이 받는 방청객 번호
for i in range(1, N + 1):
    x = arr.count(i)
    if x > real:
        real = x
        real_i = i
print(real_i)  # 실제로 가장 많은 조각을 받은 방청객의 번호를 출력