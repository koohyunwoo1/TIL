import sys
sys.stdin = open('input.txt')

# n : 현재까지 살펴본 행
def backtracking(n, sm):
    global ans

    if sm > ans:
        return

    if n == N:
        ans = min(sm, ans)
        return

    for j in range(N):
        if path[j] == False:
            path[j] = True
            backtracking(n+1, sm+arr[n][j])
            # 재귀함수 호출
            # 다음 행으로 넘어 간 후 선택되지 않은 열을 선택해 더해준다.
            path[j] = False
            # 다시 False로 바꾼다.

T = int(input())

for tc in range(1, T+1):
    N = int(input())   # 행
    arr = [list(map(int, input().split())) for _ in range(N)]

    path = [False] * N
    ans = 100 * N
    backtracking(0,0)  # 함수 호출

    print(f'#{tc} {ans}')