import sys
sys.stdin = open('input.txt')

for _ in range(1, 11):   
    # 10번의 테스트 케이스를 반복한다.
    test_case = int(input())  
    # 테스트 케이스 입력
    arr = [list(map(int, input().split())) for _ in range(100)]  
    # 100 x 100의 2차원 배열을 입력받음.

    max_sum = 0  # max_sum의 변수 값에 0을 넣어줌.

    for i in range(100):
        row_sum = sum(arr[i]) # 행의 합
        column_sum = sum(arr[j][i] for j in range(100))  # 열의 합
        diagonal_sum1 = sum(arr[i][i] for i in range(100))  # 왼쪽에서 내려오는 대각선의 합
        diagonal_sum2 = sum(arr[i][99 - i] for i in range(100)) # 오른쪽에서 내려오는 대각선의 합

        if row_sum > max_sum:   # 만약에 row_sum이 max_sum보다 크다면
            max_sum = row_sum     # row_sum은 max_sum이다.
        if column_sum > max_sum:
            max_sum = column_sum
        if diagonal_sum1 > max_sum:
            max_sum = diagonal_sum1
        if diagonal_sum2 > max_sum:
            max_sum = diagonal_sum2
                                       # 케이스의 행 열 왼,오 대각선 중에서 가장 큰 값이 max_sum으로 들어감
                                       # 10번의 테스트 케이스를 반복하므로 10개의 max_sum이 출력됨.
    print(f'#{test_case} {max_sum}')





