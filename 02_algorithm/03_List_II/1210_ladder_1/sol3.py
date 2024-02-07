import sys
sys.stdin = open('input.txt')

def search(i, j):
    # print(i, j)
    visited = [[0] * 100 for _ in range(100)]   # 방문표시용 0으로 채워진 2차원 리스트
    while i != 0:  # 탐색 시작 -> x가 0이 될 떄 까지
        for dir in [(-1, 0), (0, -1), (0, 1)]:           # 3방향 탐색   위     왼쪽    오른쪽
            ni = i + dir[0]  # 다음 탐색 대상 i 좌푯값
            nj = j + dir[1]  # 다음 탐색 대상 j 좌춋값
            # 범위를 벗어나지 않고
            # 해당 위치가 1이라 이동 가능하고
            # 이전에 방문한 적 없고
            if 0 <= ni < 100 and 0 <= nj < 100 and arr[ni][nj] == 1 and not visited[ni][nj]:
                i, j = ni, nj  # 이동
                visited[ni][nj] = 1  # 내 지금 위치 방문 표시
    return j

for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 최종결괏값
    result = 0
    # 사다리의 크기 == 100 * 100
    for j in range(100):
        # 출발 지점: i 좌표 == 99로 고정
        if arr[99][j] == 2:
            result = search(99, j)
    print(result)