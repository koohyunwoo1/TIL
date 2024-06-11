import sys
input = sys.stdin.readline

N, K = map(int, input().split())

 
pascal = [0]
for depth in range(2, N+2):
    pascal.append([0]*depth)


pascal[1] = [1, 1]

for depth in range(2, N):
    pascal[depth][0] = 1
    for idx in range(1, depth):
        pascal[depth][idx] = (pascal[depth-1][idx-1] + pascal[depth-1][idx]) % 10007
    pascal[depth][-1] = 1

if K == 0 or K == N:
    print(1)
else:
    print((pascal[N-1][K-1] + pascal[N-1][K]) % 10007)