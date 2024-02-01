import sys
sys.stdin = open('input.txt')

# 어느 사다리를 고르면 X표시에 도착하게 되는지 ?
# 100 x 100 크기의 2차원 배열로 주어진 사다리에 대해서
# 지정된 도착점에 대응되는 출발점 X를 반환하는 코드를 작성하라

# 사다리는 연속된 1로 표현 도착 지점은 2로 표현




for _ in range(1, 11):
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    # 100 x 100 크기의 2차원 배열을 만듦.

    


