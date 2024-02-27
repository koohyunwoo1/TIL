import sys
sys.stdin = open('input.txt')


'''
입력으로 데이터의 길이 N이 주어진다.
한 번의 입력으로 10개의 정수가 공백을 기준으로 나뉘어 제시되고, 이를 N번 반복하여 제시된다.
제시된 모든 정수의 합을 출력하시오.
'''


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# 최종 출력 형태 : 정수
result = 0
for numbers in arr:
    print(numbers)
    for num in numbers:
        print(num)
        result += num
print(result)