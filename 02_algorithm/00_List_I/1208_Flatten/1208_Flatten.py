import sys
sys.stdin = open('input.txt')


for i in range(1, 11):
    t = int(input())  # 덤프 횟수
    n = list(map(int, input().split()))  # 각 상자의 높이
    
    for j in range(t):
        high = max(n)  # 상자의 높이 최댓값 high로 지정
        low = min(n)   # 상자의 높이 최솟값 low로 지정
        
        if high > low:
            n[n.index(high)] -= 1  # n의 가장 높은 값 index를 찾고 상자의 높이에서 1 빼기
            n[n.index(low)] += 1  # n의 가장 낮은 값 index를 찾고 상자의 높이에서 1 더하기
            
            if max(n) == min(n):   # 상자의 높이 최댓값과 최솟값이 같으면 
                    break           # 멈춘다.

    result = max(n) - min(n)
    print(f'#{i} {result}')


