import sys
input = sys.stdin.readline

lst = []
num = 0

for _ in range(5):
    n = int(input())
    lst.append(n)
    num += n
      
lst.sort()

print(num // 5)
print(lst[2])
