x = int(input())
y = int(input())
sum = 0
for i in range(y):
    price,cnt = map(int,input().split())
    sum = sum + price * cnt

if x == sum:
    print('Yes')
else:
    print('No')