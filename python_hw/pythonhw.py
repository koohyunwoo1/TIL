# 1 
print('hello world')

# 2
print("Mary's cosmetics")

# 3
print('신씨가 소리질렀다 "도둑이야".')

# # 4
# print("C:\windows")

# 5 
print("안녕하세요.\n만나서\t\t반갑습니다")
## \n 줄바꿈 \t 탭키 

# 6
print("오늘은", "일요일")

# 7 
print('naver','kakao','sk','smasung', sep = ';')
# sep 공백사이에 내가 넣은거 작성

# 8 
print('naver','kakao','sk','samsung', sep = '/')

# 9 
print("first", end = '');print("second")

# 10
print(5/3)

# 11
삼성전자 = 50000
print(삼성전자*10)

# 12
시가총액 = 2980000000000
현재가 = 50000
PER = 15.79

print(시가총액, type(시가총액))
print(현재가, type(현재가))
print(PER, type(PER))

# 13
s = "hello"
t = "python"

print(s+'!',t)

# 14
print(2+2*3)

# 15
a = 128
print(type(a))

# 16
num_str = '720'
num_int = int(num_str)
print(type(num_str))
print(type(num_int))

# 17
num = 100
print(type(str(num)))


# 18
data = '15.79'
data = float(data)
print(type(data))

# 19
year = '2020'
year = int(year)
print(type(year))

# 20 
print(48584 * 36)

# 21
letters = 'python'
print(letters[0])
print(letters[2])

# 22
license_plate = "24가 2210"
print(license_plate[3:])
print(license_plate[-4:])   # 한칸 안띄우고 나옴

# 23
string = '홀짝홀짝홀짝'
print(string[::2])

# 24
string = 'PYTHON'
print(string[::-1])

# 25, 26
phone_number = '010-1111-2222'
print(phone_number.replace("-",""))

# 27
url = "http://sharebook.kr"
url_split = url.split('.')
print(url_split[-1])

# # 28
# lang = 'python'  # 문자열은 수정 불가
# lang[0] = 'P'
# print(lang)

# 29
string = 'abcdfe2a354a32a'
string = string.replace('a', 'A')  # replace를 통해서 새로운 변수로 할당하면 수정 가능 원본은 수정 불가능하다.
print(string)

# 30
string = 'abcd'
string.replace('b','B')
print(string)    # abcd

# 31
a = '3'
b = '4'
print(a+b)

# 32
print('HI' * 3)

# 33
print('-' * 80)

# 34
t1 = 'python'
t2 = 'java'

print((t1 +' ' + t2 + ' ')* 4)

# 35 , 36
name1 = '김민수'
age1 = 10
name2 = '이철희'
age2 = 13

print('이름: %s 나이: %d' % (name1, age1))
print('이름: %s 나이: %d' % (name2, age2))

# 37
print(f'이름 : {name1},  나이 : {age1}')
print(f'이름 : {name2} , 나이 : {age2}')

# 38 
상장주식수 = '5,969,782,550'
컴마제거 = 상장주식수.replace(',','')
print(int(컴마제거))
print(type(컴마제거))

# 39
분기 = '2020/03(E) (IFRS연걸)'
print(분기[:7])

# 40
data = '    삼성전자    '
공백제거 = data.strip()   # strip 공백제거 하는거
print(공백제거)


# 51
movie_rank = ['닥터 스트레인지', '스플릿' , '럭키']

# 52
movie_rank.append('배트맨')   # .append() : 요소 추가
print(movie_rank)

# 53
movie_rank.insert(1,'슈퍼맨')
print(movie_rank)

# # 54
# del movie_rank[3]
# print(movie_rank)

# 55
del movie_rank[2] # 삭제 한 후에 삭제 또 해야됨.
del movie_rank[2]
print(movie_rank)

# 56
lang1 = ['C','C++','JAVA']
lang2 = ['Python', 'Go', 'C#']

langs = lang1 + lang2
print(langs)

# 57
nums = [1,2,3,4,5,6,7]
print(max(nums))
print(min(nums))

# 58
nums = [1,2,3,4,5]
print(sum(nums))  # sum 리스트의 합 구하기

# 59
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))

# 60
nums = [1, 2, 3, 4, 5]
print(sum(nums) / len(nums))

# 61
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

# 62
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

# 63
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])

# 64
nums = [1, 2, 3, 4, 5]
print(nums[::-1])

# 65
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0],interest[2])

# 66 
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(' '.join(interest))

# 67
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print('/' .join(interest))

# 68
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(' \n' .join(interest))

# 69
string = "삼성전자/LG전자/Naver"
string = string.split('/')
print(string)

# 70
data = [2,4,3,1,5,10,9]
data.sort()
print(data)

# 71
my_variable = ()
print(type(my_variable))

# 72
movie_rank = ('닥터 스트레인지' , '스플릿' , '럭키')
print(movie_rank)
print(type(movie_rank))

# 73
one = (1)
print(type(one))
one = (1,)   # (1,) 쉼표로 공백을 만들어줘야지 튜플이 완성됨.
print(type(one))

# # 74
# t = (1, 2, 3)  # 튜플은 원소의 값을 바꿀수 없음.
# t[0] = 'a'

# 75
t = 1, 2, 3, 4
type(t, )
