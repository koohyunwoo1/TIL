# import sys
# sys.stdin = open('input.txt')

A, B, V = map(int, input().split())

p = V-A
# 하루에 올라갔다 미끄러져서 올라갈수있는 만큼
day = p // (A-B)
if p % (A-B) != 0:
    day += 1
print(day + 1)