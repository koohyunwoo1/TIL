import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())

arr = [list(map(str, input())) for _ in range(N)]
result = []
for i in range(N-7):
    for j in range(M-7):
        w_cnt = 0
        b_cnt = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0:
                    if arr[k][l] == 'W':
                        w_cnt += 1
                    else:
                        b_cnt += 1

                else:
                    if arr[k][l] == 'W':
                        b_cnt += 1
                    else:
                        w_cnt += 1

        result.append(w_cnt)
        result.append(b_cnt)

print(min(result))
