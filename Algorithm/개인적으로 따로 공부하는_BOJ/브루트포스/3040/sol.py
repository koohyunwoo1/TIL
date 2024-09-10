from itertools import combinations
import sys
input = sys.stdin.readline

numlist = [ int(input()) for _ in range(9)]

case = list(combinations(numlist, 7))

for i in case:
    if sum(i) == 100:
        for j in i:
            print(j)