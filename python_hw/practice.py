for arry1 in range(5):
    arry1 = 5 
    print(arry1)
'''
    5
    5
    5
    5
    5
'''


arry2 = [5 for arry2 in range(5)]
print(arry2)


'''
[5, 5, 5, 5, 5]



'''
for arry3 in range(5):
    arry3 = [5]
    print(arry3)
    
# # '''
# [5]
# [5]
# [5]
# [5]
# [5]

# '''
for arry3 in range(5):
    arry3 = [5]
    print(arry3, end= '')

    

'''
[5][5][5][5][5]

'''

for arry1 in range(5):
    arry1 = (5)
    print(arry1)

'''
5
5
5
5
5

'''

for arry1 in range(5):
    arry1 = (5,)
    print(arry1)


'''
(5,)
(5,)
(5,)
(5,)
(5,)
'''


arry1 = [5 for arry1 in range(5)]
print(arry1)


for array in range(5):
    array = [5]
    print(array)


    # 세번째
# 0은 Faulsy값
if 0:
    print('hi')
else:
    print('bye')
print()


# 네번째
for i in ['hello']:
    print(i)

for i in 'hello':
    print(i)

for i in ['hello','world']:
    print(i)


# 다섯번째 -> l을 출력
a = [['hello',2], [3,4]]

print(a[0][0][2])

# # 여섯번째 -> 사칙연산 우선순위
# 1 + 1 * 1 ** 1 - 1

# # 여덟번째
# for i, x in enumerate(['a','b','c']): #사용법, 정의  # 인덱스하고 원소로 이루어진 튜플을 만들어주는 함수
#     print(i, x)


# # 아홉번째
# def func(a, *b, **c):
    
#     print(func(a,*b,**c))
     
# 데이터를 많이 넣어두고
# 데이터가 어떤 형식으로 들어갈건지?
    
def a(n,n2):
    return n+n2

print(a(1,2), a(1,2))  # 이거 될까


# 딕셔너리 키, 벨류, 순회 공부하기
dic = {
    "부울경 : "  "1반",
    "부울경2 : "  "2반"
}

for i in enumerate(dic):
    print(i)


x = 1
y = 2
print(x>y)

def a():
    pass

# 나중에 코드를 추가하거나 예외가 발상했을 때 아무 수행을 하지 않고 넘길때 쓰는 코드



# 복수조건문 동작, 44페이지 예시
# if score == 100:
#     print("굿")
# elif score >= 95:
#     print("낫벳")


[range(3), range(3)]


