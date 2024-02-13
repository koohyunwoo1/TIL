import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            print(arr[i])






import sys
sys.stdin = open('input.txt')

def backtrack(row, selected_sum):
    global min_sum
    if row == N:  # 모든 줄에 대해 선택을 완료한 경우
        min_sum = min(min_sum, selected_sum)  # 최소값 갱신
        return
    for col in range(N):  # 현재 줄에서 선택할 수 있는 열을 탐색
        if not visited[col]:  # 아직 선택되지 않은 열인 경우
            visited[col] = True  # 해당 열을 선택했다고 표시
            backtrack(row + 1, selected_sum + arr[row][col])  # 다음 줄로 이동하고 합을 누적
            visited[col] = False  # 백트래킹을 위해 선택 표시를 되돌림

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_sum = float('inf')  # 매우 큰 값을 최소값으로 초기화
    visited = [False] * N  # 각 열의 선택 여부를 저장하는 리스트
    backtrack(0, 0)  # 백트래킹을 통해 최소 합 계산

    print(f"#{tc} {min_sum}")


