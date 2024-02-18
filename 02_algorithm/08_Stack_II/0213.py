#### 20240213
## Stack 2

# 문자열로 된 계산식이 주어질때, 스택을 이용하여 이 계산식의 값을 계산할수 있다.

# 중위표기식의 후위표기식 변환 방법 1

'''
# ex ) A*B-C/D
1단계 : ((A*B) -(C/D))
2단계 : ((A B)* (C D) / ) -
3단계 : AB*CD/-

'''


'''

fx = (6+5(2-8)/2)

'''


top = -1
stack = [0] * 100

icp = {'(':3, '*':2, '/':2, '+':1, '-':1}  # 스택 밖에서의 우선 순위
isp = {'(':0, '*':2, '/':2, '+':1, '-':1}  # 스택 안에서의 우선 순위

fx = '(6+5*(2-8)/2)'
postfix = ''
for tk in fx:
    # 여는 괄호 push, top원소보다 우선순위가 높으면 push
    if tk == '(' or (tk in '*/+-' and isp[stack[top]] < icp[tk]):
        top += 1 # push
        stack[top] = tk
    elif tk in '*/+-' and isp[stack[top]] >= icp[tk]: # 연산자이고 top원소보다 우선순위가 높지 않으면
        while isp[stack[top]] >= icp[tk]:
            top -= 1     # pop
            postfix += stack[top + 1]
        top += 1
        stack[top] = tk
    elif tk == ')':                   # 닫는 괄호면, 여는 괄호를 만날때까지 pop
        while stack[top]!= '(':
            top -= 1    # pop
            postfix += stack[top+1]
        top -= 1           #  여는 괄호 pop 해서 버림
        stack[top + 1]
    else:
        postfix += tk
print(postfix)


'''
백트래킹



'''

