import sys
sys.stdin = open('input.txt')

def is_palindrome(K):
    # 모든 문장 조회
    for i in range(100):
        # 0 부터 1까지
        # 0 부터 2까지
        # 100 - 100 + 1 (range(1))
        for j in range(100 - K + 1):
            # 가로
            '''
             words[0][0 : 0 + 100]
             첫번째 단어의 처음부터 끝까지
             words[0][1 : 1 + 99, 98]
            '''
            tmp = words[i][j:j + K]
            # 세로
            tmp2 = cross_words[i][j:j + K]

            # 가로나 세로 중에 펠린드롬이 있다면
            if tmp == tmp[::-1] or tmp2 == tmp2[::-1]:
                return K
    return 0


for _ in range(1, 11):
    tc = input()
    words = [input() for _ in range(100)]

    # 계산하기 편하도록 세로 글자만 따로 모아두기
    cross_words = []
    for i in range(100):
        tmp = ''
        for j in range(100):
            tmp += words[j][i]
        cross_words.append(tmp)


    # 어차피 가장 큰 값을 찾을 것이니 100부터 세자.
    for k in range(100, 0, -1):
        ans = is_palindrome(k)
        if ans:
            break

    print(f"#{tc} {ans}")