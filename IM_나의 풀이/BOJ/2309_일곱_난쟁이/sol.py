import sys
sys.stdin = open('input.txt')

'''
난쟁이의 키의 합은 100
'''

ki = []

for tc in range(9):
    key = int(input())
    ki.append(key)

ki_sum = sum(ki)
ki.sort()
for i in range(len(ki)):
    for j in range(i+1, len(ki)):
        if ki_sum - ki[i] - ki[j] == 100:
            for k in range(len(ki)):
                if k == i or k == j:
                    pass
                else:
                    print(ki[k])
            exit()