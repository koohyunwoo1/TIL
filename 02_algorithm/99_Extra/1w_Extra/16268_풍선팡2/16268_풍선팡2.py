import sys
sys.stdin = open('input.txt')
# 모든 풍선을 다 터트리고
# 그것의 값을 받아서
# 리스트에 담아서
# 거기서 최댓값을 찾아낸다.


T = int(input())

for testcase in range(1, T+1):
    N , M = map(int, input().split())
    flower = [list(map(int, input().split())) for _ in range(N)]

    result = []

    # 모든 풍선 다 터트림
    di = [0, 1, 0 , -1]
    dj = [1, 0 , -1, 0]
    for i in range(N):
        for j in range(M):
            count = 0
            for k in range(4):
                 ni, nj = i + di[k], j + dj[k]
                 if 0<= ni < N and 0 <= nj < M:
                    count += flower[ni][nj]

            result.append(count + flower[i][j])  # 선택한 풍선을 터뜨렸을 때의 꽃가루 수를 결과 리스트에 추가

    # 결과 출력
    max_flower = max(result)  # 꽃가루 수 중 최대값 계산
    print(f"#{testcase} {max_flower}")
#


T = int(input())  # 테스트 케이스의 개수를 입력받음

for testcase in range(1, T + 1):  # 각 테스트 케이스에 대해 반복
    print(f"Test Case #{testcase}:")  # 현재 테스트 케이스 번호 출력

    N, M = map(int, input().split())  # 꽃밭의 행과 열의 크기를 입력받음
    print(f"N: {N}, M: {M}")  # 입력받은 행과 열의 크기 출력

    flower = [list(map(int, input().split())) for _ in range(N)]  # 각 풍선의 꽃가루 양을 입력받아 2차원 리스트로 저장
    print("Flower Bed:")
    for row in flower:
        print(row)  # 입력받은 꽃밭 출력

    result = []  # 각 풍선을 터뜨렸을 때의 꽃가루 양을 저장할 리스트 초기화

    # 각 풍선을 터뜨렸을 때 인접한 풍선들의 상대적인 위치
    di = [0, 1, 0, -1]  # 행의 변화량
    dj = [1, 0, -1, 0]  # 열의 변화량

    # 꽃밭의 각 풍선을 선택하여 터뜨림
    for i in range(N):
        for j in range(M):
            count = 0  # 선택한 풍선을 터뜨렸을 때의 총 꽃가루 양을 초기화
            for k in range(4):  # 현재 풍선을 기준으로 네 방향에 있는 풍선을 확인
                ni, nj = i + di[k], j + dj[k]  # 인접한 풍선의 위치 계산
                if 0 <= ni < N and 0 <= nj < M:  # 꽃밭을 벗어나지 않는지 확인
                    count += flower[ni][nj]  # 인접한 풍선의 꽃가루 양을 합산

            print(f"Balloon at ({i},{j}): {flower[i][j]}")  # 현재 선택한 풍선의 꽃가루 양 출력
            print(f"Adjacent Flower Pollens: {count}")  # 선택한 풍선과 인접한 풍선들의 꽃가루 양 출력
            result.append(count + flower[i][j])  # 선택한 풍선을 터뜨렸을 때의 총 꽃가루 양을 결과 리스트에 추가

    # 결과 출력
    max_flower = max(result)  # 꽃가루 양 중 최대값 계산
    print(f"Max Flower Pollen: {max_flower}")  # 최대 꽃가루 양 출력
    print("-------------------------------------")  # 테스트 케이스 종료를 표시
#




