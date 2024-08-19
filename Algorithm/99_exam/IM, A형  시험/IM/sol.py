import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M1, M2 = map(int, input().split())
    weight = list(map(int, input().split()))
    weight.sort()

    tower1 = []
    tower2 = []

    if M1 > M2:
        M1, M2 = M2, M1

    while weight:
        if len(tower1) != M1:
            tower1.append(weight.pop())
        else:
            pass

        if len(tower2) != M2:
            tower2.append(weight.pop())
        else:
            break

        result = 0

        for i in range(1, len(tower1)+1):
            result += i * tower1[i-1]

        for i in range(1, len(tower2)+1):
            result += i * tower2[i-1]


    print(f'#{tc} {result}')












