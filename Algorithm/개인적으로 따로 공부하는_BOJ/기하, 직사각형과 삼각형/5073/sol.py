import sys
sys.stdin = open('input.txt')


while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    if a == b == c:
        print('Equilateral')
    elif sum((a,b,c,)) - max((a,b,c)) <= max((a,b,c)):
        print('Invalid')
    elif a == b or b == c or a == c:
        print('Isosceles')
    else:
        print('Scalene')
