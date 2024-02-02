import sys
sys.stdin = open('input.txt')

def search(i, j):
    visited = [[0] * 100 for _ in range(100)]  # 방문했는지 체크
    original_j = j  # 출발 시점의 j 좌표(original_j)
    while i != 99:  # 탐색 : x가 99가 될 때까지 순회
        for dir in [(1, 0), (0, -1), (0, 1)]:  # 3방향 탐색 => 아래 왼 오
            # 다음 탐색 대상의 i, j 좌표값
            ni = i + dir[0]
            nj = j + dir[1]
            if 0 <= ni < 100 and 0 <= nj < 100: # 범위를 벗어나지 않는다면
                if arr[ni][nj] == 1:
                    if not visited[ni][nj]:
                        i, j = ni, nj  # 이동
                        visited[ni][nj] = 1  # 방문한적 있음을 표시
                if arr[ni][nj] == 2:
                    return original_j
    # 도착은 못했지만 i == 99가 되어 조사가 끝나면 None을 return
    # => result가 None이 아니면 = 도착을 했다면
    # => (함수 실행하는)for문 종료 => 35번줄!


for _ in range(10):
    test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    result = 0

    # 사다리 크기 = 100 * 100
    for j in range(100):
        # 출발 지점 : i 좌표 0으로 고정
        if arr[0][j] == 1:
            result = search(0, j)
            if result != None:
                break

    print(f'#{test_case} {result}')