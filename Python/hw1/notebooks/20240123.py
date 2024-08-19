# 20240123

# 비시퀀스 데이터 구조

# set(세트)
# 집합 연산에서 주로 활용하는 데이터 구조
# 중복이 되지 않았고, 순서가 존재하지 않았음.(인덱스로 할수 없음.)

# 세트 메서드
my_set = set()    # 빈 set을 만들어주는 코드

my_set = {'a','b','c', 1, 2, 3}


# .add(0)
my_set.add(4)
print(my_set)

my_set.add(4)   # 4를 한번 더 넣어도 중복이 되지 않는다는것을 확인할수있음.
print(my_set)

# .remove()
my_set.remove('a')   # a가 지워짐
print(my_set)


# my_set.remove('x')    # x가 없기 때문에 에러가 뜸
# print(my_set)


# my_set.clear()
# print(my_set)    # set()    -> 빈set임

my_set = {'a','b','c', 1, 2, 3}

# .pop()
element = my_set.pop()  # 세트에서 임의의 요소를 제거하고 반환
print(element)

#.update({})
my_set.update({1,4,5})  # 세트에 다른 iterable 요소를 추가
print(my_set)

# .discard()
my_set.discard('z')   # z가 없어도 없는구나 ~ 하고 넘어감 에러가 뜨지 않음. # 반환값도 없음
print(my_set)



# 세트의 집합 메서드
set1 = {0,1,2,3,4}
set2 = {1,3,5,7,9}

print(set1.difference(set2))   # {0,2,4}   # 차집합
print(set1.intersection(set2))  # {1,3}    # 교집합
print(set1.issubset(set2))    # False  # set1 <= set2  # set1의 항목이 모두 set2에 들어있으면 True
print(set1.issuperset(set2))   # False  # set >= set2  # set1가 set2의 항목을 모두 포함하면 True
print(set1.union(set2))    # {0,1,2,3,4,5,7,9}  # 합집합

# 딕셔너리

# .clear()
person = {'name' : 'Alice' , 'age' : 25}
person.clear()
print(person)  # {} 빈 딕셔너리

# .get()
person = {'name' : 'Alice' , 'age' : 25}

print(person.get('name'))   # 해당하는 Value를 출력해줌
print(person.get('country'))  # None
print(person.get('country', 'Unknown'))

# .keys()
person = {'name' : 'Alice' , 'age' : 25}
print(person.keys())  # dict_keys(['name' , 'age'])

for k in person.keys():
    print(k)

'''
name
age
'''
# .values()
person = {'name' : 'Alice' , 'age' : 25}
print(person.values())  # dict_values(['Alice',25])

for v in person.values():
    print(v)

'''
Alice
25
'''

# items()  # key와 value 모두 출력
person = {'name' : 'Alice' , 'age' : 25}

print(person.items())
for k,v in person.items():   # dict_items([('name','Alice'),('age',25)])
    print(k,v)

'''
name Alice
age 25

'''

# .pop # 키를 제거 하고 연결됐던 값을 반환(없으면 에러나 default를 반환)
person = {'name' : 'Alice', 'age' : 25}

print(person.pop('age'))   # 25
print(person)    # {'name' : 'Alice'}
print(person.pop('country', None))   # None  # 있는 키값이 들어가도 None이 들어가면 None이 뜸
# print(person.pop('country'))   # keyError


# .setdefault

person = {'name' : 'Alice', 'age' : 25}

print(person.setdefault('name'))   # Alice
print(person.setdefault('country','KOREA'))  # KOREA  # 키가 없다면 default와 연결된 키를 
                                            # 딕셔너리에 추가하고 default를 반환
print(person)  # {'name': 'Alice', 'age': 25, 'country': 'KOREA'}


# .update
# other가 제공하는 키/값 쌍으로 딕셔너리를 갱신

person = {'name' : 'Alice', 'age' : 25}
other_person = {'name' : 'Jane', 'gender' : 'Female'}

person.update(other_person)
print(person)

person.update(age = 50)
print(person)

person.update(country = 'KOREA')
print(person)

#### hashable -> 해시가능한 자료형
#### hasing 
# 임의의 데이터를 고정된 값으로 바꾸는 것








#### literal -> 표기 가능한 값

num = 1
flo = 1.0
arr = [1,2,3]
tu = (1,2,3)



#### immutable -> 불변형


