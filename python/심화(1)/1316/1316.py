import sys
sys.stdin = open('input.txt')

N = int(input())
cnt = N


for tc in range(1,N+1):
    str = input()

    for i in range(len(str)-1):
        if str[i] == str[i+1]:
            continue
        elif str[i] in str[i+1:]:
            cnt -= 1
            break

print(cnt)