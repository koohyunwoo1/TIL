import sys
sys.stdin = open('input.txt')




# 브루트 포스 방식으로 푸는 함수
def brute_force(pattern, target):
    result = 0
    pattern_index = 0
    target_index = 0

    while target_index < len(target):
        if pattern[pattern_index] != target[target_index]:
            result += 1
            pattern_index = -1
        pattern_index += 1
        target_index += 1
        if pattern_index == len(pattern):
            pattern_index = 0
            result += 1
    return result

# --- 아래는 시간이 남아 돈다면...

# KMP 방식으로 푸는 함수
def KMP(pattern, target):
    def make_lps():
        lps = [0] * len(pattern)
        for i in range(1, len(pattern)):
            if pattern[lps[i-1]] == pattern[i]:
                lps[i] = lps[i - 1] + 1
        lps[0] = -1
        return lps
    lps = make_lps()

    result = 0
    target_index = 0
    pattern_index = 0
    while target_index < len(target):
        if target[target_index] != pattern[pattern_index]:
            pattern_index = lps[pattern_index]
            result += 1

        target_index += 1
        pattern_index += 1

        if pattern_index == len(pattern):
            result += 1
            pattern_index = 0
    return result


# 보이어 무어 방식으로 푸는 함수
def boyer_moore(pattern, target):
    lps = {pattern[i]: len(pattern) - i - 1 for i in range(len(pattern))}
    result = 0
    pattern_index = len(pattern)
    target_index = 0
    while target_index <= len(target) - pattern_index:
        for p_idx in range(pattern_index-1, -1, -1):
            if target[target_index+p_idx] != pattern[p_idx]:
                skip_cancle_range = lps.get(target[target_index+p_idx], len(pattern))
                target_index += skip_cancle_range
                result += 1
                break
        else:
            target_index += 1
            result += 1

    return result

T = int(input())

for tc in range(1, T+1):
    A, B = input().split()
    result = len(A) - (A.count(B) * len(B)) + A.count(B)
    result = brute_force(B, A)
    result = KMP(B, A)
    result = boyer_moore(B, A)
    print(f'#{tc} {result}')