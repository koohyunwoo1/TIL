import sys
sys.stdin = open('input.txt')

def subtree(root, left, right):
    if not root:
        # 우선 root의 값이 존재하지 않다면 
        # 서브노트의 값도 없는거기 때문에
        return 0
        # 0을 반환해준다.
    stack = [root]
        # root 를 넣어준 상태에서 stack을 만들어준다.
        # 넣어준 이유는 해당 노드부터 시작을 하기 위해서 넣어줌.
    count = 0

    while stack:
        # 스택이 빌 때까지
        node = stack.pop()
        # print(node)
        # 여기 node에는 root의 서브트리가 들어간다.
        count += 1


        # 트리가 왼쪽 오른쪽 둘다 있을수도 있기 때문에
        # 왼쪽 오른쪽 다 살펴봄
        if left[node]:
            # 왼쪽 노드가 비어있지 않으면
            stack.append(left[node])
            # 스택에 추가
        
        if right[node]:
            # 오른쪽 노드가 비어있지 않으면
            stack.append(right[node])
            # 스택에 추가
    return count

T = int(input())
# 우선 트리를 한번 만들어보자
for tc in range(1, T+1):
    E, N = map(int, input().split())
    # E  부모 자식 노드 번호 쌍의 개수
    # N  서브트리의 루트
    lst = list(map(int, input().split()))

    ch1 = [0] * (E+2)  # 자식노드들을 저장해주기 위해 0으로 초기화된 리스트 만듦
    ch2 = [0] * (E+2)

    for i in range(0, len(lst), 2):
        # 부모노드와 자식노드를 만들어줌
        p, c = lst[i] , lst[i+1]
        # 트리를 한번 만들어보자
        if ch1[p] == 0:
            # ch1이 비어있으면
            ch1[p] = c
            # 자식노드를 넣어주고
        else:
            ch2[p] = c
            # 비어있지 않으면
            # 다른 자식노드에 넣어준다.
    result = subtree(N, ch1, ch2)
    print(f'#{tc} {result}')
        




