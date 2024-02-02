import sys
sys.stdin = open('input.txt')

T = float(input())

inch = 2.54
result = (T) * inch
print((f'{T} inch => {result}'))