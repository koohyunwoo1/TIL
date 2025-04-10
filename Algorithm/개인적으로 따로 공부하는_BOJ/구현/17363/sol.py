import sys
input = sys.stdin.readline

R, C = map(int, input().split())
A, B = map(int, input().split())


for i in range(R * A): # 행별로 반복
    for j in range(C * B):  # 열별로 반복
        if ((i % (A*2)) < A) == ((j % (B*2)) < B): # X가 처음 나오는 행 조건과 X가 나오는 열 조건 교집합
            print("X", end="") # 교집합을 만족할때 X출력
        else:
            print(".", end="") # 나머지 .출력
    print("")