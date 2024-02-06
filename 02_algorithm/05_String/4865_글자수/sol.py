import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(1, T+1):
    str1 = str(input())
    str2 = str(input())

    max_result = 0

    for i in str1:
        result = 0
        for j in str2:
            if i == j:
                result += 1

        if max_result < result:
            max_result = result

    print(f'#{_} {max_result}')


    