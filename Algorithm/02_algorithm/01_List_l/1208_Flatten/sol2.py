import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())  # 덤프횟수
    height = list(map(int, input().split()))


    result = 0

    for i in range(N):
        high = max(height)
        low = min(height)

        if high > low:
            height[height.index(high)] -= 1
            height[height.index(low)] += 1

            if high == low:
                break


    print(f'#{tc} {max(height) - min(height)}')