# p 26 도전문제
# 트리형태를 보고, 직접 재귀호출 코드 구현하기

# Branch : 2
# Level(기저조건) : 3
'''
def run(level):
    if level == 3:
        return

    for i in range(2):
        run(level + 1)


run(0)

'''


# 중복순열
'''
path = []

def KFC(x):
    if x == 2:  # x가 기저조건일때
        print(path)  # 출력해준다.
        return

    for i in range(3):
        path.append(i)
        KFC(x + 1)
        path.pop()

KFC(0)
'''


# 마지막 Level에 도착할 때 마다 출력하면 된다.
# 중복순열 [1,1,1] ~ [6,6,6] 까지 출력하는 코드를 재귀호출로 구현하자.
# branch = 6 level = 3
'''
path = []

def KFC(x):
    if x == 3:
        print(*path)
        return

    for i in range(1, 7):
        path.append(i)
        KFC(x + 1)
        path.pop()

KFC(0)
'''

## 이미 사용한 숫자인지 아닌지 구분하는 코드


## [도전] 중복 순열과 순열 구현하기
# N개의 주사위를 던져 나올 수 있는 모든
# 중복 순열(type 1)과 순열(type 2)를 출력 하시오

# 입력)
# 2 1 # N, Type
'''
path = []
used = []
N = 0

def type1(x):
    if x == N:  # x가 기저조건일때
        print(path)  # 출력해준다.
        return

    for i in range(1, 7):
        path.append(i)
        type1(x + 1)
        path.pop()

def type2(x):
    if x == N:  # x가 기저조건일때
        print(path)  # 출력해준다.
        return

    for i in range(1, 7):
        if used[i] == True : continue
        used[i] = True
        path.append(i)
        type2(x + 1)
        path.pop()
        used[i] = False

used = [False for _ in range(7)]
N, type = map(int, input().split())

if type == 1:
    type1(0)
if type == 2:
    type2(0)
'''