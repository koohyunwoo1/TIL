import sys
input = sys.stdin.readline

N = int(input())

cntA = 0
cntB = 0

for i in range(N):
    A, B = map(int, input().split())

    if A > B:
        cntA += 1
    elif B > A:
        cntB += 1
    else:
        0
        
    
print(cntA, cntB)