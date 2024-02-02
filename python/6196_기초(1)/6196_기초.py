import sys
sys.stdin = open('input.txt')

t = input()
t1 = t + t
t2 = t + t + t
t3 = t + t + t + t
result = int(t) + int(t1) + int(t2) + int(t3)
print(result)
