# import sys
# sys.stdin = open('input.txt')

'''
K = 탐색 대상이 된 원소 번호
result = 최종 결괏값 (부분집하을 구하기 위함 type(list))
cnt = 부분집합의 합이 몇이냐 ?
'''
def powerset(K, result, cnt):
    global count
    count += 1
    # 배열 arr에 양의 정수만 들어있고, 지속적을 누적해 나갈것이다.
    if cnt > 10:  # 한번이라도 누적합이 10을 넘어섰다면 , 앞으로는 조사하는 의미가 없다.
        return  # 더 조사하지말고 돌아가
    # print(result)
    # 언제까지 조사 할 것이냐
    # K 번째 원소를 사용한 경우, 사용하지 않은 경우
    if K == N:    # 모든 원소에 대해 조사를 마쳤다면,
        # print(result)
        if cnt == 10:    # 다음 조건 : 부분집합의 합이 10인 경우만,if cn == 10
            print(result)
        return # 조사 종료
    else:
        # K번째 원소를 사용한 경우
        powerset(K+1, result + [arr[K]], cnt + arr[K])
        # K번째 원소를 사용하지 않은 경우
        powerset(K+1, result, cnt)

N = 10 # 원소의
arr = list(range(1,11))
count = 0
# 0번 요소부터 조사, 공집합, 누적합 0
powerset(0, [], 0)
print(count)