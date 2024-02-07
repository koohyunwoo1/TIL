import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    s = list(map(str, input()))
    s_len = len(s)
    stack = []
    
    for i in range(s_len):
        # s의 길이만큼 반복해준다.
        if not stack:
            # 만약 stack이 비어있다면
            stack.append(s[i])
            #  stack에 s[i]번째 원소들을 더해준다.
        else:
            # 만약 stack이 비어있지 않다면
            if stack[-1] == s[i]:
                # stack의 제일 마지막 값과 s의 i번째 원소의 값이 같다면
                stack.pop()
                # stack의 제일 마지막 값을 제거해주고 s의 i번째 원소는 추가하지 않는다.
            else:
                stack.append(s[i])

    result = len(stack)
    print(f'#{tc} {result}')
    

    
