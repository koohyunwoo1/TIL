import sys
sys.stdin = open('input.txt')

pattern = {
    (2, 1, 1): 0,
    (2, 2, 1): 1,
    (1, 2, 2): 2,
    (4, 1, 1): 3,
    (1, 3, 2): 4,
    (2, 3, 1): 5,
    (1, 1, 4): 6,
    (3, 1, 2): 7,
    (2, 1, 3): 8,
    (1, 1, 2): 9
}

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [list(map(int, input())) for _ in range(N)]
    print(f'#{tc}', end=' ')
    for x in range(N):
        if len(set(data[x])) == 2:
            y = 0
            tmp = []
            while y != M:
                if (x == 0 and data[x][y] == 1) or (data[x][y] == 1 and data[x-1][y] == 0):
                    c = {0: 0, 1: 0, 2: 0, 3: 0}
                    for k in range(4):
                        while data[x][y] == (k % 2):
                            c[k] += 1
                            y += 1
                    tmp.append(pattern[(c[1], c[2], c[3])])
                y += 1
            result = 0
            for i in range(8):
                if i % 2:
                    result += tmp[i]
                else:
                    result += tmp[i] * 3
            if result % 10:
                print(0)
            else:
                print(sum(tmp))
            break

