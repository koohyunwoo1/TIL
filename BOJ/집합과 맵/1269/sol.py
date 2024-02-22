import sys
sys.stdin = open('input.txt')

num1, num2 = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

print(len(A-B)+len(B-A))