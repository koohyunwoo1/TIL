import sys
sys.stdin = open('input.txt')

def search(i, j):
    # print(i, j)
    visited = [[0] * 100 for _ in range(100)]   # 방문표시용 0으로 채워진 2차원 리스트
    orginal_j = j   # 출발 시점의 j 좌표 기록
    while i != 99:  # 탐색 시작 -> x가 99가 될 떄 까지
        for dir in [(1, 0), (0, -1), (0, 1)]:           # 3방향 탐색   아래     왼쪽    오른쪽
            ni = i + dir[0]  # 다음 탐색 대상 i 좌푯값
            nj = j + dir[1]  # 다음 탐색 대상 j 좌춋값
            if 0 <= ni < 100 and 0 <= nj < 100:  # 새 좌푯값이 범위를 벗어나지 않고 이동 가능하다.
                if arr[ni][nj] == 1:
                    if not visited[ni][nj]:  # 다음 위치 방문한 적 없으면 이동
                        i, j = ni, nj  # 이동
                        visited[ni][nj] = 1  # 내 지금 위치 방문 표시

                if arr[ni][nj] == 2:  # 도착점
                    # print(orginal_j)
                    return orginal_j
    # 도착점 도착은 못헀지만 i == 99가 되어서 조사가 끝나면 None을 return 헀다...
    return

for _ in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 최종결괏값
    result = 0
    # 사다리의 크기 == 100 * 100
    for j in range(100):
        # 출발 지점: i 좌표 == 0으로 고정
        if arr[0][j] == 1:
            result = search(0, j)
            if result != None:
                break
    print(f'#{_} {result}')