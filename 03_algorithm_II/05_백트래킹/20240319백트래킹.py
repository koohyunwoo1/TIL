### 20240319 

# 백트래킹
# 완전탐색 + 가지치기
# 가능성이 없는(볼 필요 없는) 경우의 수를 제거하는 기법

# 중복된 순열
# 1~3 까지 숫자 배열

# 재귀함수 => 특정 시점으로 돌아오는게 핵심 
# 재귀 함수 팁
# 파라미터: 바로 작성 X, 구조를 먼저 잡으면 자연스럽게 필요한 변수들이 보인다.

arr = [i for i in range(1, 4)]
path = [0] * 3

'''
def dfs(cnt):
    # 기저 조건
    # 이 문제에서는 3개를 뽑았을 때 까지 반복
    if cnt == 3:
        print(*path)
        return

    # 들어가기 전
    # 다음 재귀 호출
    #    - 다음에 갈 수 있는 곳들은 어디인가 ?
    #    - 이 문제에서는 1,2,3 세 가지 경우의 수가 존재


    # 기본코드
    # path[cnt] = 1
    # dfs(cnt + 1)
    # 
    # path[cnt] = 2
    # dfs(cnt + 1)
    # 
    # path[cnt] = 3
    # dfs(cnt + 1)


    for i in range(len(arr)):
        path[cnt] = arr[i]
        dfs(cnt + 1)
    # 갔다와서 할 로직

dfs(0)
'''



# 순열
# 123, 132, 213, 231, 312, 321
# 조건 : 숫자는 한번만 사용해라


def backtraking(cnt):
    if cnt == 3:
        print(*path)
        return


    for i in range(len(arr)):
        # 갈 수 없을때만, 아래 코드를 실행하라.

        if arr[i] in path:
            continue

        path[cnt] = arr[i]
        backtraking(cnt + 1)
        path[cnt] = 0


backtraking(0)

