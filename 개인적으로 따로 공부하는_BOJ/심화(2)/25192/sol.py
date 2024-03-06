import sys
sys.stdin = open('input.txt')

N = int(input())
st = set()
cnt = 0

for i in range(N):
    name = input()

    if name != 'ENTER':
        if name not in st:
            cnt += 1
            st.add(name)

    elif name == 'ENTER':
        st.clear()


print(cnt)