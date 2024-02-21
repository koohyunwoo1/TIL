import sys
sys.stdin = open('input.txt')

str = input()

if str == str[::-1]:
    print('1')
else:
    print('0')