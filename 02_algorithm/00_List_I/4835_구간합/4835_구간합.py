import sys
sys.stdin = open('sample_input.txt')

t = int(input())

for i in range(1, t+1):
    N , M = map(int, input().split())  # 정수의 개수 N과 구간의 개수 M
    a = list(map(int, input().split()))
    # 정수 
    result = []
    # 빈 리스트를 하나 만들어줌.
    for j in range(N - M + 1):
        # j가 전체 한번씩 돌수 있음.
        total = sum(a[j:j+M])
        result.append(total)

    max_sum = max(result)
    min_sum = min(result)

    print(f'#{i} {max_sum-min_sum}')
        















