import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for i in range(1,T+1):
     N = int(input())
     a = list(map(int, input().split()))
     result = max(a) - min(a)
     print(f'#{i} {result}')


