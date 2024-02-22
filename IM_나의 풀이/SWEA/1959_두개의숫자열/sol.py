import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N < M:  # 항상 N이 크다
        A, B = B, A
        N, M = M, N
        B = B + [0] * (N-M)
        # print(B)
        # A가 B보다 항상 크다
    max_sum = 0  # 최대 합을 저장할 변수, 음수 무한대로 초기화
    for i in range(N-M+1):
        temp_sum = 0  # 현재 부분 수열에서의 곱의 합을 저장할 변수
        for j in range(M):
            temp_sum += A[j+i] * B[j]  # 대응되는 원소끼리 곱하여 합에 더함
        max_sum = max(max_sum, temp_sum)  # 최대 합 갱신

    print(f'#{tc} {max_sum}')  # 결과 출력

