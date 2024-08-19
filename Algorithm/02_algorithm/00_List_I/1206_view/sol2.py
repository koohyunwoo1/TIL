import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    height = list(map(int, input().split()))

    result = 0

    for i in range(2, N-2):
        if (height[i] > height[i+1]
            and height[i] > height[i+2]
            and height[i] > height[i-1]
            and height[i] > height[i-2]
        ):
            a1 = height[i] - height[i+1]
            a2 = height[i] - height[i+2]
            a3 = height[i] - height[i-1]
            a4 = height[i] - height[i-2]

            lst = [a1, a2, a3, a4]

            result += min(lst)


    print(f'#{tc} {result}')

