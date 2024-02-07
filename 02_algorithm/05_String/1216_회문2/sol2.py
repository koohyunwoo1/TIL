import sys
sys.stdin = open('input.txt')


# n * n 행렬에서 m 길이의 팰린드롬 찾기
def palindrome(array, m):
    # 아까 여러개로 이루어진 것을 하나로 만듬
    for row in array:  # 1 ~ 100
        for start in range(100 - m + 1):
            for i in range(m // 2):
                if row[start + i] != row[start + m - 1 - i]:
                    break
            else:
                return True
    return False


def find_loggest_vertical(vertical):
    # 큰 거부터 줄여나가면서 찾음
    max_v = 1
    # max_v 보다 큰 것만 탐색
    for m in range(1, 101):
        # 만약 max_h보다 2큰 회문이 존재하지 않는다면 그것보다 큰 회문 존재 x
        if m > max_v + 2:
            print(m, max_v)
            # max_h 반환
            return max_v
        # 만약 m 길이의 회문이 존재하면
        if palindrome(vertical, m):
            max_v = m

    return max_v


def find_loggest_horizontal(horizontal, max_v):
    # Horizontal에서 큰거부터 하나하나 줄여나가면서 계산하면 시간이 너무 오래걸림
    max_h = max_v
    # max_v 보다 큰 것만 탐색
    for m in range(max_v, 101):
        # 만약 max_h보다 2큰 회문이 존재하지 않는다면 그것보다 큰 회문 존재 x
        if m > max_h + 2:
            # max_h 반환
            return max_h
        # 만약 m 길이의 회문이 존재하면
        if palindrome(horizontal, m):
            # max_h = m 할당
            max_h = m
    return max_h

T = 10
for _ in range(1, T + 1):
    t = int(input())
    horizontal = [input() for _ in range(100)]
    # zip으로 전치 행렬 생성
    vertical = list(zip(*horizontal))

    max_v = find_loggest_vertical(vertical)

    if max_v != 100:
        max_h = find_loggest_horizontal(horizontal, max_v)

    result = max(max_v, max_h)
    print(f'#{t} {result}')