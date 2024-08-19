import sys
sys.stdin = open('input.txt')

while True:
    # 조건이 맞지 않을때까지 무한반복
    try:
        print(input())
    except:
        break