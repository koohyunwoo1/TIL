import sys
sys.stdin = open('input.txt')

'''
도착하게 되는 출발점의 x 좌표를 출력
'''
T = 10

for tc in range(1, T+1):
    testcase = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 도착지점의 인덱스를 찾자
    col, row = 0, 0
    for i in range(100):
        if arr[99][i] == 2:
            col = 99
            row = i
            break

    while col != 0:  # 출발점에 도착할때까지
        if row -1 > 0 and arr[col][row-1] == 1:
            while row-1 > 0 and arr[col][row-1] == 1:
                row -= 1

        elif row +1 < 100 and arr[col][row+1] == 1:
            while row +1 < 100 and arr[col][row+1] == 1:
                row += 1



        col -= 1

    print(f'#{tc}', row)




