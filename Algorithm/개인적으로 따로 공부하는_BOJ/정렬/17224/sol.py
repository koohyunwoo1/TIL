import sys
input = sys.stdin.readline

N, M, K = map(int,input().split())
score=[]
for i in range(N):
    sub1,sub2 = map(int, input().split())
    if sub2<=M:
        score.append(140)
    elif sub1<=M:
        score.append(100)
score=sorted(score,reverse=True)
print(sum(score[:K]))