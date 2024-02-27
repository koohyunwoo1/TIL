number = int(input('양의 정수를 입력해주세요.: '))
while number <= 0:
    if number == -9999:
        print('프로그램을 종료합니다.')
        break
    if number < 0:
        print('음수를 입력했습니다.')
    else:
        print('0은 양의 정수가 아닙니다.')
    number = int(input('양의 정수를 입력해주세요.: '))
print('잘했습니다!')


numbers = [1, 3, 5, 6, 7, 9, 10, 11]
found_even = False
for num in numbers:
    if num % 2 == 0:
        print('첫 번째 짝수를 찾았습니다:', num)
        found_even = True
        break
if not found_even:
    print('짝수를 찾지 못했습니다')
