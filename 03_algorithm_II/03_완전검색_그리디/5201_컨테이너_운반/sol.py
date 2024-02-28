import sys
sys.stdin = open('input.txt')
'''
옮겨진 화물의 전체 무게가 얼마인지 ?
적재용량이 큰 트럭에 무게가 큰거를 넣으면 될듯 ?
트럭당 한개의 컨테이너를 운반 할수 있으니깐
화물이 싣지 못한 트럭이 있을수도 있고, 또한 남는 화물이 있을수도 있음.
컨테이너를 한 개도 옮길 수 없는 경우 0을 출력한다.
'''
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # N : 컨테이너 수 M : 트럭 수
    weight = sorted(list(map(int, input().split())), reverse=True)  # 무게
    truck = sorted(list(map(int, input().split())))   # 적재용량

    result = 0
    t = truck.pop()  # 제일 무거운게 pop됨

    for w in weight:
        if w <= t:   # 무게가 적재용량보다 작다면 싣을수 있기 때문에
            result += w  # result에 그 무게만큼 계속 더해준다.
            if truck:  # truck이 남아있으면
                t = truck.pop()
            else:
                break


    print(f'#{tc} {result}')
