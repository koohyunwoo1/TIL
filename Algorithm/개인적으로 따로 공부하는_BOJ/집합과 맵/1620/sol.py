import sys
sys.stdin = open('input.txt')

'''
문제가 알파벳 - > 포켓몬 번호를 말해야함
문제가 숫제 -> 포켓몬 이름을 말해야함
'''
N, M = map(int, input().split())

pokemon = dict()
number = dict()

for i in range(1, N+1):
    po = input()
    pokemon[i] = po
    number[po] = i

for j in range(M):
    target = input()

    if target.isalpha() == True:
        print(number[(target)])

    if target.isdigit() == True:
        print(pokemon[int(target)])