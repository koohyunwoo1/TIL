import sys
sys.stdin = open('input.txt')


# 자기 기준 양쪽 2개씩 자기 높이보다 낮아야됨.
# 주변 2칸내에 가장 높은 값이 내 현재 값보다 낮을경우 두값차이 구해야함.
# 그래야 조망권 ? 이 보여서


for i in range(1, 11):
    N = int(input())
    N_height = list(map(int, input().split())) # 건물 높이의 리스트

    result = 0

    for j in range(2, N-2):  # 건물 높이가 0인것은 제외 시키고 반복문 돌리기
        if (N_height[j] > N_height[j-1]    
            and N_height[j] > N_height[j-2]  
            and N_height[j] > N_height[j+1]   
            and N_height[j] > N_height[j+2]  
        ):   # j번쨰의 건물이 양옆 두개의 건물보다 높이가 높을때 
            a1 = N_height[j] - N_height[j-1]    
            a2 = N_height[j] - N_height[j-2]    
            a3 = N_height[j] - N_height[j+1]    
            a4 = N_height[j] - N_height[j+2]    
            a_list = [a1, a2, a3, a4]   # 앞의 두건물과 뒤의 두건물 높이 차이의 리스트
            result = result + min(a_list)  # 두개의 값 차이가 가장 작은것
    print(f'#{i} {result}')




