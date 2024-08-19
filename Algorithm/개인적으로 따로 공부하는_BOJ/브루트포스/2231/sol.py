import sys
sys.stdin = open('input.txt')

'''
216 - 1 - 9 - 8 = 198

'''
N = int(input())  # 분해합을 입력값으로 받았음.

for i in range(1, N+1):
    num = list(map(int, str(i)))
    num_sum = sum(num) + i

    if num_sum == N:
        print(i)
        break

    if i == N:
        print(0)


