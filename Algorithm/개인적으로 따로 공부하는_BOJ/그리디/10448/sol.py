import sys
input = sys.stdin.readline

tri = [i * (i + 1) // 2 for i in range(1, 46)]  
eur = [0] * 1001

for i in tri:
    for j in tri:
        for k in tri:
            num = i + j + k
            if num <= 1000:
                eur[num] = 1 

t = int(input())
for _ in range(t):
    print(eur[int(input())])