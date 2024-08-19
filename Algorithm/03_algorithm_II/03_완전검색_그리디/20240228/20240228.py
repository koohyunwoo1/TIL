
'''
민철이에게는 3명의 친구가 있다.
{MIN, CO, TIM}

함께 영화관에 갈 수 있는 멤버를 구성 하고자 한다.
모든 경우를 출력해보자
'''

'''
arr = ['O', 'X']
path = []
name = ['MIN', 'CO', 'TIM']

def print_name():
    print('{', end = '')
    for i in range(3):
        if path[i] == 'O' :
            print(name[i], end= ' ')
    print('}')


def run(lev):
    if lev == 3:
        print_name()
        return


    for i in range(2):
        path.append(arr[i])
        run(lev + 1)
        path.pop()

run(0)
'''

'''
부분집합 바이너리 카운팅을 이용해서
도전과제 문제를 풀어보자

민철이는 친구 {A,B,C,D,E}가 있다
이 중 최소 2명 이상의 친구를 선정하여
함께 카페에 가려고 한다.

총 몇가지의 경우가 가능할까 ?

'''

'''
arr = ['A', 'B', 'C', 'D', 'E']
n = len(arr)

def get_count(tar):
    cnt = 0
    for i in range(n):
        # 1비트 1인지 확인
        if tar & 0X1:
            cnt += 1
        tar >>= 1
    return cnt

result = 0
for tar in range(1 << n):
    if get_count(tar) >= 2:   # bit가 2개이상 1이라면 -> 2명 이상이라면
        result += 1

print(result)
'''


### 조합

# 5명중 3명 뽑는 조합은 3중 for문으로 구현이 가능하다.
'''
arr = ['A', 'B', 'C', 'D', 'E']

for a in range(5):
    start1 = a + 1
    for b in range(start1, 5):
        start2 = b + 1
        for c in range(start2, 5):
            print(arr[a], arr[b], arr[c])
'''

'''
arr = ['A', 'B', 'C', 'D', 'E']
path = []

n = 3
def run(lev, start):
    if lev == n:
        print(path)
        return


    for i in range(start, 5):
        path.append(arr[i])
        run(lev + 1, i + 1)
        path.pop()

run(0, 0)
'''
'''
주사위 던지기
주사위 눈금N개를 던져나 나올 수 이쓴
모든 조합을 출력하시오

N = 3 일때 출력 결과
'''
'''
N = 3
path = []

def func(lev, start):
    if lev == N:
        print(path)
        return

    for i in range(start, 7):
        path.append(i)
        func(lev + 1, i)
        path.pop()
func(0, 1)

'''
'''
도전문제
이 문제는 그리디로 풀 경우,
어떤 기준으로 접근해야, 대기시간의 누적합이 최소가 될지 고민해보고
직접 구현해보자

A 15 B 30 C 50 D 10

'''
'''
person = [15, 30, 50, 10]
n = len(person)
person.sort()
sum = 0
left_person = n - 1

for turn in range(n):
    time = person[turn]
    sum += left_person * time
    left_person -= 1
print(sum)
'''

'''
도전문제
이 문제를 그리디로 접근한다면,
어떤 기준으로 선택을 하는 것이 좋을까 ?

도둑은 보물들이 있는 창고에 침입하였다.
도둑은 최대 30KG까지 짐을 담아갈 수 있다.

물건의 개수(N) 그리고 물건 별 무게(W)와 가격(P)이 주어질 때,
어떤 물건을 담아야, 도둑이 최대 이득을 볼 수 있을지 구하시오.

무게 값
5    50
10   60
20   140


이 문제는 그리디로 풀 수 없다
'''

'''
n = 3
target = 30
things = [(5, 50), (10, 60), (20, 140)]

things.sort(key = lambda x: (x[1] / x[0]), reverse = True)

sum = 0

for kg, price in things:
    per_price = price / kg
    # 만약 가방에  남은 용량이 얼마 되지 않는다면, 물건을 잘라 가방에 넣고 끝낸다
    if target < kg:
        sum += target * per_price
        break


    sum += price
    target -= kg

print(int(sum))
'''

'''
회의실 문제
무엇을 기준으로 회의를 선택해야 최대한 많은 횟수의 회의가 될지 고민해보자.

위와 같이 6개의 희망 회의가 있는 경우, 최대 3번의 회의가 가능하다
'''





