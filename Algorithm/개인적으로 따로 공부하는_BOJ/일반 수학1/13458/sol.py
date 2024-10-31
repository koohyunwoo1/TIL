import sys
input = sys.stdin.readline

n=int(input())
n_cnt=list(map(int,input().split()))
b,c=map(int,input().split())
res=0
for i in range(n):
    n_cnt[i]-=b
    res+=1
    if n_cnt[i]>0:
        if n_cnt[i]%c==0:
            res+=(n_cnt[i]//c)
        else:
            res+=(n_cnt[i]//c+1)

print(res)
