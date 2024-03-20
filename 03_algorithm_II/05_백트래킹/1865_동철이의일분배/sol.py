import sys
sys.stdin = open('input.txt')

'''
r => 조사 대상 행
acc => 누적 값 (확률)
'''

def search(r, acc):
    global result
    # 언제까지 탐색하느냐 ?
    if r == N:
         # problem solving code
        result = max(result, acc)
        pass
    for i in range(N): # 모든 열에 대해서 조사를 한다.
        if not visited[i]:
            visited[i] = 1
            search(r + 1, acc * arr[r][i])
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            arr[i][j] = arr[i][j] / 100
    # 이미 사용한적 있는지 체크하기 위한
    visited = [0] * N
    # 최종 결과값
    result = 0
    # 누적값의 초기값을 1로 설정해야한다.
    search(0,1)
    print(f'#{tc} {(result * 100)}')
