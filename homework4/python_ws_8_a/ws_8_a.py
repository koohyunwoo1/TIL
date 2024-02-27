data = {'name': '홍길동'}
try:
    if not data['age']:
        print(data['age'])
    else:
        print('data에는 age라는 키가 없습니다.')
        data['age'] = 30
        print(data)
except KeyError:
    print('data에는 age라는 키가 없습니다.')
    data['age'] = 30
    print(data)
      
# 아래에 코드를 작성하시오.



arr = ['반갑', '하세요', '안녕']
for i in range(4):
    try:
        print(arr.pop())
    except IndexError:
        print('더 이상 pop 할 수 없습니다.')
print(arr)
# 아래에 코드를 작성하시오.



word = '3.15'
try:
    print(int(word))
except ValueError:
    print('정수로 변환 가능한 값을 입력해 주세요.')
# 아래에 코드를 작성하시오.