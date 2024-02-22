import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))

    result = 'Possible'
    acc = 0
    # 매 초마다 만들 수 있는 빵의 개수를 세어나가므로
    # 별도의 기록 과정 필요 없이 계산가능
    # 마찬가지로 정렬되어있으므로, 시간 순서에 따른 누적값이 어긋날 경우 없음
    for idx in sorted(arr): # 손님 방문 시간 정렬
        acc += 1            # 누적 방문 손님 기록
        bread = (idx//M)*K  # 손님 방문 시간에 만들 수 있는 최대 빵 수 계산
        bread -= acc        # 해당 시간까지 누적되어 온 손님 수 만큼 빵 감소
        if bread < 0:       # 빵 모자라면 실패
            result = 'Impossible'
            break
    print(f'#{tc} {result}')