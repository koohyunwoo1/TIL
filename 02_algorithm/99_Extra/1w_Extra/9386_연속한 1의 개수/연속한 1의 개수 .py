import sys
sys.stdin = open('input.txt')

# N개의 0과 1로 이루어진 수열에서 연속한 1의 개수 중
# 최대값을 출력하는 프로그램

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num_list = list(input().split('0'))
    # 0을 기준으로 짜른다.
    
    count = []
    for num in num_list:
        count.append(len(num))
    
    print(f'#{tc} {max(count)}')
    
