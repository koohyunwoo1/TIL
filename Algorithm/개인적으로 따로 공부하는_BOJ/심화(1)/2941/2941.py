import sys
sys.stdin = open('input.txt')

alphabet = ['c=','c-','dz=','d-','lj','nj','s=','z=']

str = input()

for i in alphabet:
    str = str.replace(i, '0')

print(len(str))

