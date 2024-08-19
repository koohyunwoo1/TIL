import sys
sys.stdin = open('input.txt')

'''
부모노드는 왼쪽 자식노드보다는 커야되고 오른쪽 자식노드보다는 작아야 한다.
그러니깐 제일 왼쪽부터 차례대로 넣어주면 된다.

이진 탐색 트리의 루트에 저장된 값과, N/2번 노드(N이 홀수인 경우 소수점 버림)을 출력
'''
## 중위 순회를 해야할듯 ?
# 왼쪽 자식노드, 부모노드, 오른쪽 자식노드 순으로 방문한다.


# 루트노드가 존재하는 조건은 N보다 작거나 같아야한다.
# n * 2 왼쪽노드 n* 2 + 1 오른쪽 노드
def inorder(n):
    if n:
      inorder()  

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    
    lst = [0] * (N + 1)
        

    print(f'#{tc} {inorder(1)} {inorder(N // 2)}')


