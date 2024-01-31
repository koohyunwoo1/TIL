import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1,T+1): 
    # 1,2, .... T까지 순회한다.
    N = int(input())  
    # 칠 할 영역의 개수 N
    arr = [[0 for _ in range(10)] for _ in range(10)] 
    # 10 x 10의 0의  행렬을 만들어줌.
    purple_count = 0
    # purple_count를 0으로 지정해줌.
    for _ in range(N):
    # 칠 한 영역의 수 N만큼 반복해준다.
        r1, c1, r2, c2, color = map(int, input().split())
       # 행  열  행  열    색깔
        for i in range(r1, r2+1):  # 행 i가 r1 부터 r2까지 반복해준다.
            for j in range(c1, c2+1):   # 열 j가 c1부터 c2까지 반복해준다.
                if arr[i][j] == 0:  # 행렬이 0이면
                    arr[i][j] = color  # color로 칠해준다.
                elif arr[i][j] != color:  # 행렬이 color가 아니면(중복된값), 정보에서 값이 겹치지 않는다고 함.
                    arr[i][j] = 3   # 값을 3으로 해준다.
                    if arr[i][j] == 3:  # 행렬 값이 3이면
                        purple_count += 1   # 1씩 올라감.

    
    
    print(f'#{test_case} {purple_count}')

                     
                     

































        

    

    
    


    



    




    
