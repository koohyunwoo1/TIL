import sys
input = sys.stdin.readline


# 모든 굴다리 밝힐 수 있는지 확인하는 함수
def is_possible(location, height):
    # 첫번째 가로등
    if height - location[0] < 0:
        return False
    # 사이 가로등
    for i in range(1, M):
        if location[i] - location[i-1] > 2 * height:
            return False
    # 마지막 가로등
    if N - location[-1] > height:
        return False
    # 모든 조건 통과하면 모두 밝힌 것
    return True


# N 입력
N = int(input())

# M 입력
M = int(input())

# 가로등 위치 입력
x = list(map(int, input().split()))

# 이분탐색 시작, 끝 정의
start = 1
end = N

# 정답 높이 정의
answer = N

# 이분탐색 실행
while start <= end:
    # 중앙값 정의
    mid = (start + end) // 2

    # 모두 밝히는 것 가능하면 높이 줄여보기
    if is_possible(x, mid):
        answer = mid
        end = mid - 1

    # 불가능하면 높이 늘리기
    else:
        start = mid + 1

# 결과 출력
print(answer)
