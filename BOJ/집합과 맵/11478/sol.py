import sys
sys.stdin = open('input.txt')

S = input()
lst = []

for i in range(len(S)):
    text = ''
    for j in range(i, len(S)):
        text += S[j]
        lst.append(text)

print(len(set(lst)))

