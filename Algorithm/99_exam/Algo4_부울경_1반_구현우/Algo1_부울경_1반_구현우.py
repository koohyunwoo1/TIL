T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    
    # 델타탐색을 위해 델타 설정
    di = [1,-1,0,0]
    dj = [0,0,1,-1]
    
    # 최대값을 구해주기 위해 0으로 초기화해준다.
    max_cnt = 0
    for i in range(N):
        for j in range(N):
            # 상하좌우로 몇번의 보너스 점수를 얻는지
            cnt = 0
            # 두칸씩 이동하기 때문에 범위를 1,2로 설정해주고
            for k in range(1, 3): 
                # 상하좌우 돌아준다.
                for l in range(4):
                    ni = i + di[l] * k
                    nj = j + dj[l] * k
                    # 범위를 벗어나지 않는선에서 정리하고
                    if 0 <= ni < N and 0 <= nj < N:
                        cnt += arr[ni][nj]

            # 마지막에 상하좌우 값 + 자기 자신의 값
            if max_cnt < cnt + arr[i][j]:
                max_cnt = cnt + arr[i][j]

    print(f'#{tc} {max_cnt}')
