import sys
sys.stdin = open('input.txt')

T = int(input())
 
for i in range(1,T+1):
    string = input()
    if string == string[::-1]:
        result = 1
    else:
        result = 0
 
    print(f'#{i} {result}')