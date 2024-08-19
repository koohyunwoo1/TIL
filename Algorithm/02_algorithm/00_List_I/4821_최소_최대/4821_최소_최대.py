import sys
sys.stdin = open('sample_input.txt')

t = int(input())

for i in range(1,t+1):  # 1부터 t까지 반복해주겠다.
    N = int(input())  # 양수의 개수
    a = list(map(int, input().split()))  # 양수 한칸씩 공백 있이 
    result = max(a) - min(a)  # 가장 큰 값과 가장 작은값을 빼준다
    print(f'#{i} {result}')





























# T = int(input())
# for i in range(1,T+1):
#      N = int(input())
#      a = list(map(int, input().split()))
#      result = max(a) - min(a)
#      print(f'#{i} {result}')


