'''
# 부분 집합의 합

def f(i, k, s, t): # k개의 원소를 가진 배열 A, 부분집합 합이 t인 경우를
    # global cnt
    # cnt += 1
    if s == t:   # 모든 원소에 대해 결정하면
        for j in range(k):
            if bit[j]:
                print(A[j], end = ' ')
        print()   # 부분집합 출ㄺ
    elif i == k:   # 모든 원소를 고려했으나 s! = t
        return
    elif s > t:    # 고려한 원소의 합이 t보다 큰 경우
        return
    else:
        # for j in range(1, -1, -1):
        #     bit[i] = j
        #     f(i+1, k, t)
        bit[i] = 1
        f(i+1, k, s+A[i], t)
        bit[i] = 0
        f(i+1, k, s , t)

N = 10
A = [1,2,3,4,5,6,7,8,9,10]
bit = [0] * N # bit[i]는 A[i]가 부분집합에 포함되는지 표시
f(0, N, 0, 10)
# print(f'cnt :', cnt)


'''