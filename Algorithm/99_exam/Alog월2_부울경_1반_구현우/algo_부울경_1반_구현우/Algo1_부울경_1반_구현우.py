T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    # 돌의 개수 N과 뒤집기 작업의 총 횟수 M
    lst = list(map(int, input().split()))

    # lst = 돌의 초기 상태
    for _ in range(M):
        i, j, w = map(int, input().split())

        # 기준 위치(i), 작업할 돌의 개수(j), 수행할 작업번호(W)

        if w == 1:
            for k in range(i-1, min(i+j-1, N)):
                # 범위 벗어나는거 방지 위해 min값 설정
                lst[k] = 1 - lst[k]

        elif w == 2:
            for l in range(i-1, min(i+j-1, N)):
                # 범위 벗어나는거 방지 위해 min값 설정
                lst[l] = lst[i-1]

        elif w == 3:
            start = i -1
            end = min(i+j-1, N)
            # 범위 벗어나는거 방지 위해 min값 설정
            while start < end:
                # start 값이 end의 값보다 작아지면 반복문 종료
                if lst[start] == lst[end]:
                    # 대칭이면
                    lst[start] , lst[end] = 1- lst[start] , 1- lst[end]
                    # 바꿔준다.
                    start += 1
                    end -= 1
                else:
                    continue
            break

    print(f'#{tc}', end=' ')
    print(*lst)

