import sys
sys.stdin = open('input.txt')

case = 0

while True:
    L, P,  V = map(int, input().split())

    if L == 0 and P == 0 and V == 0:
        break

    max_days = (V // P) * L + min(V % P, L)
    case += 1

    print(f'Case {case}: {max_days}')