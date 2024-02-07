import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    n, str_ = input().split()
    n = int(n)

    stack = []

    for i in str_:
        if not stack:
            # stack이 비어있으면
            stack.append(i)
            # stack에 i원소를 집어 넣어준다.
        else:
            # stack이 비어있지 않으면
            if stack[-1] != i:
                # stack의 마지막 원소가 i번째 원소랑 같지 않다면
                stack.append(i)
                # 넣어주고
            else:
                # 같으면
                stack.pop()
                # 마지막 원소를 제거해준다.
    result = ''.join(stack)
    print(f'#{tc} {result}')