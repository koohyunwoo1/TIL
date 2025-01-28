tree = list(map(int, input().split()))
answer = [1, 2, 3, 4, 5]

while True:
    for i in range(len(tree)-1):
        if tree[i] > tree[i+1]:
            tree[i], tree[i+1] = tree[i+1], tree[i]
            print(" ".join(map(str, tree)))

    if tree == answer:
        break