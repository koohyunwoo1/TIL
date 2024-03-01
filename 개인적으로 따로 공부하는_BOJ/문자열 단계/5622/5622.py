import sys
sys.stdin = open('input.txt')

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

alpha = list(input())
result = 0

for i in alpha:
    for j in dial:
        if i in str(j):
            num = dial.index(j) + 3
            result += num
print(result)

