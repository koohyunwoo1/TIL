import sys
sys.stdin = open('input.txt')

# 문제
# N x N 크기의 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램을 만드시오.
# 회문은 1개가 존재하는데, 가로뿐만 아니라 세로로 찾아질수도있다.

T =int(input())

for tc in range(1,T+1):
    N , M = map(int, input().split())
    # M  :  길이
    arr = [input() for _ in range(N)]


    # 가로 방향에서 회문 찾기

    for i in range(N):
        for j in range(N - M + 1): 
            if arr[i][j:j+M] == arr[i][j:j+M][::-1] :
                # 단어가 회문이라면
                final_result = arr[i][j:j+M]
                # 그 회문인 단어를 result에 넣겠다.

    
    # 세로 방향에서 회문 찾기
    result = []

    for i in range(N):
        sero = ''
        for j in range(N):  
            sero += arr[j][i]
        result.append(sero)

    for i in range(N):
        for j in range(N - M + 1):
            if result[i][j:j+M] == result[i][j:j+M][::-1]:
                final_result = result[i][j:j+M]


    print(f"#{tc} {final_result}")












