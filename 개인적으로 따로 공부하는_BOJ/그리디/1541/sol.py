import sys
input = sys.stdin.readline

x = input().split('-')
num = [] #새 숫자가 들어갈 list
#print(x)
for i in x:
    count = 0
    sp = i.split('+')
    #print(sp)
    for j in sp:
        count += int(j)
    num.append(count)

result = num[0]
for j in range(1,len(num)):
    result -= num[j]
print(result)
