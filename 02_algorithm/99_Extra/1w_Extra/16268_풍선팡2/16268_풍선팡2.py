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
                 if 0 <= ni < N and 0 <= nj < M:
                    count += flower[ni][nj]
            
            result.append(count + flower[i][j])  # 선택한 풍선을 터뜨렸을 때의 꽃가루 수를 결과 리스트에 추가

    # 결과 출력
    max_flower = max(result)  # 꽃가루 수 중 최대값 계산
    print(f"#{testcase} {max_flower}") 
                
            


    

            







