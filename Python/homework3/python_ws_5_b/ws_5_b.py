data_1 = 'qweqwYadnOyjnsaU4trwg asjnaAn245krRmkfE 42grTasdnHasdnvEasdn asdevadnBasdanEsdkqefqefvaSasdqaeeqqvedwt5hfbsdT24tewfd'
'''
예시코드
arr = [1, 2, 3, 4, 5]
for num in arr:
    print(num, end='')
출력결과 : 12345
'''
# 아래에 코드를 작성하시오.

for i in data_1:
    if i.isupper():
        print(i, end = '')
    elif i == " ":
        print(i, end = "")

# 5 12 29 37
print()
data_2 = '걉파반샤팝다푸거맥파바자들퍼바배들밥샵파누타히매니배사바파힘다브사부힙헤베내테치대내'
# data_2.find('내')   # 37
# data_2.find('힘')   # 29
# data_2.find('들')   # 12 
# data_2.find('다')   # 5

arr = []
for i in '내힘들다':
    arr.append(data_2.find(i))
# arr.append(data_2.find('내'))
# arr.append(data_2.find('힘'))
# arr.append(data_2.find('들'))
# arr.append(data_2.find('다'))
print(arr)
arr.sort(reverse=False)
print(arr)

for i in arr:
    print(data_2[i], end = '')

# 아래에 코드를 작성하시오.
