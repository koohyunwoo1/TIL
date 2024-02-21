import sys
sys.stdin = open('input.txt')
'''
길이가 짧은순으로 하고
길이가 같으면 사전 순으로 한다.
'''
T = int(input())

word = [str(input()) for i in range(T)]
word = list(set(word))

word.sort()
word.sort(key=len)

for i in word:
    print(i)