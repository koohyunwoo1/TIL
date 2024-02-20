import sys
sys.stdin = open('input.txt')

# T번 만큼 반복 할 수 있도록
T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))
    # print(N, ai)
    print(f'#{test_case} {max(ai) - min(ai)}')
