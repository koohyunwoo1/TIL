import sys
input = sys.stdin.readline
n = int(input())
word = [input().rstrip() for _ in range(n)]

for i in range(n):
    for j in range(i, n):
        if word[i][::-1] == word[j]:
            print(len(word[i]), word[i][len(word[i])//2])
            exit()