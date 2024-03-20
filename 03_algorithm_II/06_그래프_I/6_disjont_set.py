# 1~6번까지 노드가 존재.
# 1. make_set
def make_set(n):
    return [i for i in range(n)]

# 1~6번까지를 사용하기 위해 7개 생성(0번은 버림)
parents = make_set(7)
print(parents)
# 2. find_set: 대표자를 찾아보자
# - 부모 노드를 보고, 부모 노드도 연결이 되어 있다면 다시 반복
# - 언제까지 ? 자기 자신이 대표인 데이터를 찾을 때 까지
def find_set(x):
    # 자기 자신이 대표네 ? 끝
    if parents[x] == x:
        return x

    # 위의 조건이 걸리지 않았다 == 대표자가 따로 있다.
    return find_set(parents[x])

# 3. union
def union(x, y):
    x = find_set(x)
    y = find_set(y)

    # 이미 같은 집합에 속해있다면 continue
    if x == y:
        return

    # 다른 집합이라면 합침
    # 예 ) 더 작은 루트노트에 합쳐라~
    if x < y:
        parents[y] = x
    else:
        parents[x] = y



union(1, 3)
union(2, 3)
union(5, 6)
print(parents)
union(1, 5)
print(parents)

