import sys
sys.stdin = open('input.txt')

def backtrack(row, n, now_sum, visited):
    # row : 현재 탐색 중인 행의 인덱스
    # n : 행렬의 크기
    # now_sum : 현재까지 선택한 요소들의 합
    # visited : 각 열을 방문했는지 여부를 나타내는 리스트
    global min_sum  # 최소합을 전역변수로 선언
    if row == n:  # i가 배열의 수와 일치하면
        # 현재 합과 (지금까지)최소합 값을 비교
        if now_sum < min_sum:
            min_sum = now_sum  # 현재합이 더 작으면 대체
    elif now_sum > min_sum:
        return  # 현재 부분합이 더 크면 탐색 중지 (Pruning)
    else:
        for col in range(n):
            if not visited[col]:  # 방문 전인 컬럼
                visited[col] = 1  # 방문처리
                # 다음 row로 넘어가고, now_sum에 값을 더해주고, visited 갱신
                backtrack(row + 1, n, now_sum + num[row][col], visited)
                visited[col] = 0  # 함수 적용 후 초기화 (재검색 할 수 있도록)


T = int(input())
for tc in range(T):
    n = int(input())
    num = [list(map(int, input().split())) for _ in range(n)]
    min_sum = 100  # 값을 대체해주기 임의의 큰 수 대입
    visited = [0] * n

    backtrack(0, n, 0, visited)  # 함수시작
    print(f'#{tc + 1} {min_sum}')


# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     lst = [list(map(int, input().split())) for _ in range(N)]
#
#     min_sum = 0
#
#     for i in range(N):
#         min_sum += min(lst[i])
#         min_index = lst[i].index(min(lst[i]))
#         # print(min_index)
#         for j in range(N):
#             for k in range(N):
#                 if j == min_index and k != i:
#                     lst[k][j] = 9999
#
#     print(lst)
#
#     print(f'#{tc} {min_sum}')
