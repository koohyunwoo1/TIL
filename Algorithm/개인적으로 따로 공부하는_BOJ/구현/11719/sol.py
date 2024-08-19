import sys
print(sys.stdin.read())

while True:
    try:
        print(input())
    except EOFError:
        break