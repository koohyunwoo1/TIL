import sys
sys.stdin = open('sample_input.txt')

t = int(input())

for i in range(1, t+1):
    N , M = map(int, input().split())
    numbers = list(map(int, input().split()))
    # numbers 해준이유 
    # 배열 된 정수를 list에 담아줌.
    result = []
    # 빈 리스트를 하나 만들어줌.
    for j in range(N - M + 1):
        # j가 전체 한번씩 돌수 있음.
        total = sum(numbers[j:j+M])
        result.append(total)

    max_sum = max(result)
    min_sum = min(result)

    print(f'#{i} {max_sum-min_sum}')
        















