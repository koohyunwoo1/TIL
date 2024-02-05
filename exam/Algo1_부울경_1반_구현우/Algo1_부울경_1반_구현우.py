import sys
sys.stdin = open('algo1_sample_in.txt')


# 어떤 칸을 맞히면 그 칸의 상하좌우 4칸의 점수를 더한 값에서
# 맞힌 칸의 점수를 뺸다

# 양수면 보너스 점수
# 음수면 보너스 점수는 0점
# 이때 얻은 보너스 점수가 짝수면 보너스 점수는 2배
# 가장자리 칸을 맞혀 상하좌우 중 일부 칸이 없는 경우 보너스 점수느 0점


T = int(input())
# 테스트 케이스 인풋받음
for test_case in range(1, T+1):
    N = int(input())
    Aij = [list(map(int, input().split())) for _ in range(N)]

    bonus = []
    
    for i in range(1,N-1):
        for j in range(1,N-1):
            # 가장자리가 아니면
            # 보너스포인트는 상하좌우에서 자기값을 뺀거다
            bonus_point = (Aij[i+1][j] + Aij[i-1][j] + Aij[i][j+1] + Aij[i][j-1]) - Aij[i][j]

            if bonus_point % 2 == 0:
                # 짝수라면
                bonus_point *= 2
                # 2배해주고
            elif bonus_point < 0:
                # 0보다 작으면
                bonus_point = 0
                # 0점이다.

            bonus.append(bonus_point)

    bonus = sorted(bonus, reverse=True)
    print(f'#{test_case} {bonus[0]}')
