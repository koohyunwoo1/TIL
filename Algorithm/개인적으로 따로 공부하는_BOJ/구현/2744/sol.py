import sys
input = sys.stdin.readline

for i in input():
    if i.isupper():
        print(i.lower(), end='')
    else:
        print(i.upper(), end='')