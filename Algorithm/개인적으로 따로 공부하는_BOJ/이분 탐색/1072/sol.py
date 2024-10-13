import sys
input = sys.stdin.readline

x,y=map(int,input().split()) 
z=(100*y)//x 
left=0 
right=x 
res=x 
if z>=99: 
    print(-1)
else: 
    while left<=right: 
        mid=(left+right)//2 
        if (100*(y+mid))//(x+mid)>z: 
            res=mid 
            right=mid-1 
        else: 
            left=mid+1
    print(res)
