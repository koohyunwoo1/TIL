import sys
sys.stdin = open('input.txt')
# 문자열 str1에 포함된 글자들이 str2에 몇개씩 들어있는지 찾고 
# 그 중 가장 많은 글자의 개수를 출력하는 프로그램을 출력하시오.
T = int(input())
# 테스트 케이스 인풋받음.
for _ in range(1, T+1):
    str1 = input()
    str2 = input()
    # str1, str2를 인풋받음.
    max_result = 0
    # max_result라고 
    for i in str1:
        result = 0
        # 제일 중요함
        for j in str2:
            if i == j:
                result += 1

        if max_result < result:
            max_result = result

    print(f'#{_} {max_result}')


    