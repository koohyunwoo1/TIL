import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # 입력받은 문자열
    word = list(input())
    # 스택 생성
    stack = []
    top = -1
    # 결과값
    result = 1
    # 문자열 전체 순회
    # print(stack)
    for i in range(len(word)):
        # print(word[i])
        # 괄호에 포함된 경우에만 push나 pop을 할 예정
        if word[i] in ['{', '}', '(', ')']:
            # 만약 괄호를 여는 문자라면
            if word[i] in ['(', '{']:
                # push
                top += 1
                stack.append(word[i])
            # 아니라면 괄호를 닫는 문자다
            else:
                # 만약 스택에 문자가 없다면 실패
                if top == -1:
                    result = 0
                    break
                # 만약 top에 있는 괄호가 (라면
                elif stack[top] == '(':
                    # )라면 pop
                    if word[i] == ')':
                        top -= 1
                        stack.pop()
                    # 아니라면 (}니깐 실패
                    else:
                        result = 0
                        break
                # 만약 top에 있는 괄호가 {라면
                elif stack[top] == '{':
                    # }라면 pop
                    if word[i] == '}':
                        top -= 1
                        stack.pop()
                    # 아니라면 {)니깐 실패
                    else:
                        result = 0
                        break
        # print(stack)
    # 스택에 괄호가 남아있다면 실패
    if top > -1:
        result = 0


    print(f'#{tc}', result)
