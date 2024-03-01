import sys
sys.stdin = open('input.txt')

hour, min = map(int, input().split())

if min >= 45:
    print(hour, min-45)
elif hour>0 and min<45:
    print(hour-1, min+15)
else:
    print(23,min+15)