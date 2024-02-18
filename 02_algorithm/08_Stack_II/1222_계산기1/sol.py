import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    num_len = int(input())
    num = list(map(int, input().split('+')))

    print(f'#{test_case} {sum(num)}')

    