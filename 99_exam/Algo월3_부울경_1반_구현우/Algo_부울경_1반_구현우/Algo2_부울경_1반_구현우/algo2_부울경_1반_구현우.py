import sys
sys.stdin = open('algo2_sample_in.txt')

'''
최대 다리 수와 이때의 건설비용을 출력
'''

T = int(input())

for tc in range(1, T+1):
    N, V = map(int, input().split())
    # N : 섬의 수, V : 예산
    C = list(map(int, input().split()))
    C.sort()
    # C : 건설 비용
    bridge_cnt = 0  # 최대 다리 수
    idx = 0
    min_money = 0  # 최소 건설 비용

    while min_money <= V and idx < N:
        bridge_cnt += 1
        min_money += C[idx]
        idx += 1

        if min_money > V:
            bridge_cnt -= 1
            min_money -= C[idx - 1]

    print(f'#{tc} {bridge_cnt} {min_money}')



