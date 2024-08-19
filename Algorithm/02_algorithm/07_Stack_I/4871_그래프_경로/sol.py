import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    # v = 노드의 수, e = 연결의 수
    v, e = map(int, input().split())
    # 연결 상태를 보여준다.
    adj = [[] for _ in range(v+1)]
    # 방향이 있는 노드이므로 adj[출발] = [도착] 으로 정의해준다.
    for _ in range(e):
        start, end = map(int, input().split())
        adj[start].append(end)
    from_node, to_node = map(int, input().split())
    # 가능한 길이 있는지 여부를 확인
    is_Check = False
    # DFS를 활용하기위해 stack을 설정하고 시작점을 넣는다.
    stack = [from_node]
    # 특정 연결이 양방향 노드일 수도 있기 때문에 방문 여부를 체크하는 리스트를 만든다.
    check_list = [False] * (v+1)
    while stack :
        # stack의 최상단 값을 꺼낸다.
        check_node = stack.pop()
        # 꺼낸 값이 목표와 같다면 도달할 방법이 있으므로 반복을 종료
        if check_node == to_node:
            is_Check = True
            break
        # 꺼낸 값이 목표와 다를 때 아직 방문하지 않은 노드라면 노드와 연결된 점들을 stack에 넣어준다.
        elif not check_list[check_node]:
            stack.extend(adj[check_node])
        # 방문했다는 표시를 해준다.
        check_list[check_node] = True
    # 경로가 존재하면 1을 출력
    if is_Check :
        print(f"#{tc+1} 1")
    # 존재하지 않으면 0 출력
    else:
        print(f"#{tc+1} 0")