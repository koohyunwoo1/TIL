import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(1,T+1):
    str1 = str(input())
    str2 = str(input())
     
    if str1 in str2:
        result = 1
    else:
        result = 0

    print(f'#{i} {result}')