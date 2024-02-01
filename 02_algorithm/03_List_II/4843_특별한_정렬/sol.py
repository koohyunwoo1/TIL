import sys
sys.stdin = open('input.txt')
# import pprint

T = int(input()) # 테스트 케이스 개수

for _ in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))

    ai = sorted(num)  # 오름차순으로 정렬
    bi = sorted(num, reverse = True) # 내림차순으로 정렬

    ai_lst = []
    bi_lst = []

    for i in range(len(ai) // 2):  
        # 가장 큰 값 1/2 개를 순회함.
        ai_lst.append(ai.pop())
        # ai_lst라는 빈 리스트에다가 큰 값 5개를 넣어준다.
        # pop을 이용해서 가장 큰 값부터 5개의 원소만 제거한후 다시 반환한다.
    for i in range(len(bi) // 2): 
        # 가장 작은 값 1/2 개를 순회함.
        bi_lst.append(bi.pop())
        # bi_lst라는 빈 리스트에다가 작은 값 5개를 넣어준다.
    
    # print(ai_lst)    
        # 가장 큰값이 뽑혀있는 리스트
    # print(bi_lst)   
        # 가장 작은값이 뽑혀있는 리스트

    result = []

    for i in range(5): 
        # 5번 까지만 반복
        # 주어진 문제에서 결과를 10개까지 출력하라고 했기 때문
        result.append(bi[i])
        result.append(ai[i])

    print(f'#{_} {result}')

