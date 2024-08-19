import sys
sys.stdin = open('input.txt')

'''
N X N 크기의 미로에서 출발지에서 목적지에 도착하는 경로가
존재하는지 확인하는 프로그램을 작성하시오.
도착할 수 있으면 1, 아니면 0을 출력한다
2는 출발지이며 3은 도착지이며 0은 통로 1은 벽이다.
'''

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    stack = []
    visited = [[False ] * N for _ in range(N)]

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start_i = i
                start_j = j

            if arr[i][j] == 3:
                goal_i = i
                goal_j = j
    
    stack.append([start_i, start_j])

    while stack:
        i,j = stack.pop()
        for k in range(4):
            nx = dx[k] + i
            ny = dy[k] + j

            if nx == goal_i and ny == goal_j:
                visited[nx][ny] = True
                break

            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] == 0 and visited[nx][ny] == False:
                    stack.append([nx, ny])
                    visited[nx][ny] = True
    
    if visited[goal_i][goal_j] == True:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
                    
            
