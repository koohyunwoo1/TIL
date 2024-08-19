import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 최종결괏값
    result = 0
    # 아직 내가 원하는 지점 찾지 못했음
    check = False
    # 사다리의 크기 == 100 * 100
    for i in range(100):
        for j in range(100):
            # 출발 지점:
            if i == 0:
                if arr[i][j] == 1:
                    # 방문표시용 0으로 채워진 2차원 리스트
                    # visited = [[0] * 100] * 100
                    visited = [[0] * 100 for _ in range(100)]
                    # 출발 시점의 j 좌표 기록
                    orginal_j = j
                    while i != 99: # 탐색 시작 -> x가 99가 될 떄 까지
                        # print(i, j)
                        # x, y = i, j
                        # 3방향 탐색   아래     왼쪽    오른쪽
                        for dir in [(1, 0), (0, -1), (0, 1)]:
                            # 현재위치 i, j를 기준으로 dir[0], dir[1]
                            ni = i + dir[0]  # 다음 탐색 대상 i 좌푯값
                            nj = j + dir[1]  # 다음 탐색 대상 j 좌춋값
                            if 0 <= ni < 100 and 0 <= nj < 100 and arr[ni][nj] == 1: # 이동 가능하다.
                                if not visited[ni][nj]: # 다음 위치 방문한 적 없으면 이동
                                    visited[i][j] = 1 # 내 지금 위치 방문 표시
                                    i, j = ni, nj   # 이동

                            if 0 <= ni < 100 and 0 <= nj < 100 and arr[ni][nj] == 2: # 도착점
                                result = orginal_j
                                check = True
                                break
                        # 내가 한번이라도 도착점이 2인곳에 도달했다면
                        if check:
                            break
            # 내가 한번이라도 도착점이 2인곳에 도달했다면
            if check:
                break
        # 내가 한번이라도 도착점이 2인곳에 도달했다면
        if check:
            break
    print(result)