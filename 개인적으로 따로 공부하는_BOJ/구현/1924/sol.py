import sys
sys.stdin = open('input.txt')

x, y = map(int, input().split())
date = ['SUN','MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
date2 = [31,28,31,30,31,30,31,31,30,31,30,31]
day = 0

for i in range(x-1):
    day += date2[i]

ans = (day + y) % 7
print(date[ans])
