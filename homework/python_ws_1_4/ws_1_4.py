# 원주율
# 파이썬 변수명
# 기본 : snake_case
# 전부 대문자 snake_case : 상수
# BASE_DIR
PI = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
# 반지름
r = 15

pi_is = '원주율 : '
radius_is = '반지름 : '
print(f'원주율 : {PI}')
print(f'{pi_is} {PI}')
print(f'{pi_is}{PI}')
# '원주율 : ' + str(3.141592....)
# '원주율 : ' + '3.141592....'
# print('원주율 : 3.141592...')
print(pi_is + str(PI))

print(f'{radius_is}{r}')

# 반지름 * 2 * 원주율
perimeter = '원의 둘레 : '
# 반지름 * 반지름 * 원주율
area = '원의 넓이 : '

print(perimeter, r * 2 * PI)
print(area , r * r * PI)