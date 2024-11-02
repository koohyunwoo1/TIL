import sys
S = sys.stdin.readline().strip() + ' ' # 마지막에 공백을 더해주자
stack = [] # 저장해줄 스택
result = '' # 결과물 출력
cnt = 0 # 괄호 안에 있는지 여부
for i in S : # 받은 문자열 찾아보자
    if i == '<' : # <를 만나면
        cnt = 1 # 지금 괄호 안에 있음 표시
        for _ in range(len(stack)): #괄호 만나기 이전 stack 애들 비워주고 다 뒤집어서 더해!
            result += stack.pop()
    stack.append(i)
    
    if i == '>' : # >를 만나면
        cnt = 0 # 지금 괄호 빠져 나왔음 표시
        for _ in range(len(stack)): # 괄호 안에 있는 애들은 뒤집지 말고 더해!
            result += stack.pop(0)

    if i == ' ' and cnt == 0: # 공백을 만나고 괄호 밖에 있다면
        stack.pop() # 들어간 공백 뺴주고
        for _ in range(len(stack)): # 뒤집어서 더해!
            result += stack.pop()
        result += ' ' # 마지막에 공백 살려주기
print(result)
