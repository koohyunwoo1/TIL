import sys
sys.stdin = open('input.txt')

T = int(input()) # 테스트 케이스의 개수

for test_case in range(1, T+1):
    result = [] # 구간합들을 넣을 리스트 선언
    N, M = map(int, input().split()) # 총 열의 개수와 각 구간의 길이를 입력 받는다
    sum_arr = list(map(int, input().split())) # 숫자 배열을 입력받는다
    for i in range(len(sum_arr)):  # 배열을 순회한다
        if len(sum_arr[i:i+M]) == M: # 배열의 개수가 사용자가 더하고자 하는 배열과 같다면
            result.append(sum(sum_arr[i:i+M])) # 결과에 append 한다

    print(f'#{test_case} {max(result) - min(result)}')