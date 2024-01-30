import sys
sys.stdin = open('sample_input.txt')

# 0번부터 출발해 종점인 N번 정류장까지 이동하고,
# 한번 충전으로 최대한 이동할수있는 정류장 수 K
# 충전기가 설치된 M개의 정류장 번호가 주어짐.
# 최소한 몇번의 충전을 해야 종점(N에 도착할수있는지
'''
gas : 이동 가능 횟수
now : 현재 정류장 위치
cnt : 충전 횟수
'''

def go(gas, now, cnt):
    global result
    # 지금까지 충전한 횟수가
    # 언젠가 누군가 종착점에 도착할때까지 들었던 충전 횟수보다 크다면
    # 더 이상 조사할 이유 없음
    if cnt > result:
        return
    # 정류장 종착점 도착하면 멈춤
    if now == N:
        # 지금까지 충전한 횟수를 result에 넣을거임.
        result = cnt
        return 
    if station[now]:
        # 충전 했으니 이동 가능 횟수 K
        # 충전하고 다음칸으로 갈때 가스 1 든다.
        go(K-1, now+1, cnt+1)
    if gas:
    # 현재 위치에 충전소가 없으면 그냥 한칸 이동
    # 가스가 남아 있다면
        go(gas-1, now+1, cnt)


T = int(input())

for i in range(1,T+1):
    K,N,M = map(int, input().split())
    data = list(map(int, input().split()))

    station = [0] * (N+1)
    # 정류장에 충전소 위치 표기
    for index in range(M):
        station[data[index]] = True
    # 최종 결과값 : 최소 충전 횟수가 조건
    # 최악의 경우를 상정
    result = N+1
    # 출발시 최대치 가스 가지고 시작 : K
    # 시작 위치 0
    # 충전 횟수 0
    go(K, 0, 0)
    # 모든경우의 수 다 확인 했는데 result가 그대로다 ? 도착못했다
    if result == N+1:
        reuslt = 0
    print(result)
    
         

# 0 -> 10까지 이동하는데 3번까지 한번에 이동할 수 있으며 
# 충전기가 설치된 정류장은 M의 수

# 한번 이동할수있는 정류장 수 3 k
# 종점이 10 N
# 충전기가 설치된 정류장 5 M
# 정류장 번호 1 3 5 7 9 M_number