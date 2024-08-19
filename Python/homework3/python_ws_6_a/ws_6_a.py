my_set = {'가', '나', (0, 0)}  # 순서가 없어서 랜덤으로 배치됨.
my_dict = {
        '가': 1, 
        (0, 0): '튜플도 키값으로 사용가능'
    }

# 아래에 코드를 작성하시오.

for key in my_set:
    value = my_dict.get(key, 'None')
    print(value)



var = (1,2,3,'A')
my_dict[var] = '변수로도 키 설정 가능'
print(my_dict)







for key in my_set:
    if key in my_dict:
        value = my_dict[key]
        print(value)
    else:
        print(None)


var = (1,2,3,'A')
my_dict[var] = '변수로도 키 설정 가능'
print(my_dict)



    