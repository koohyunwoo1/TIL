import sys
sys.stdin = open('input.txt')


for _ in range(1,11):
    N = int(input())
    # 찾아야 하는 회문의 길이
    arr = [input() for _ in range(8)]
    # 8x8 배열 만들어줌
    result_count = 0

    # 가로에 회문이 있는지 확인
    for i in range(8):
        for j in range(8-N+1):
            # 배열의 범위를 벗어나는 것을 방지하고자 반복하는 횟수를 설정한다.
            if arr[i][j:j+N] == arr[i][j:j+N][::-1]:
                # arr 슬라이싱한 문자열이 거꾸로한 문자열과 같다면
                result_count += 1
                

    # 세로 줄 가로로 돌리기
    result = []

    for i in range(8):
        sero = ''
        for j in range(8):
            sero += arr[j][i]
        result.append(sero)
        # print(result)
    
    # 세로에 회문이 있는지 확인
    for i in range(8):
        for j in range(8-N+1):
            if result[i][j:j+N] == result[i][j:j+N][::-1]:
                result_count += 1
                

    print(f'#{_} {result_count}')
    

