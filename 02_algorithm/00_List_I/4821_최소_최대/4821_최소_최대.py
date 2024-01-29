import sys
sys.stdin = open('sample_input.txt')

t = int(input())

for i in range(1,t+1):  # 1부터 t까지 반복해주겠다.
    N = int(input())  # 
    a = list(map(int, input().split()))
    result = max(a) - min(a)
    print(f'#{i} {result}')



























# T = int(input())
# for i in range(1,T+1):
#      N = int(input())
#      a = list(map(int, input().split()))
#      result = max(a) - min(a)
#      print(f'#{i} {result}')


