# 아래 클래스를 수정하시오.
class UserInfo:
    def __init__(self):
        self.user_data = {}

    def get_user_info(self):
        try:
            self.name = input('이름을 입력하세요 : ')
            self.age = int(input('나이를 입력하세요 : '))
        except ValueError:
            self.name = None
            self.age = None
            
    def display_user_info(self):
        if self.name != None and self.age != None:
            print('사용자 정보 : ')
            print('이름 :', self.name)
            print('나이 :', self.age)
        else:
            print('나이는 숫자로 입력해야 합니다.\n사용자 정보가 입력되지 않았습니다.')
        
            
        
user = UserInfo()
user.get_user_info()
user.display_user_info()




# 강사님 코드

class UserInfo():
    def __init__(self):
        self.user_data = {}

    def get_user_info(self):
        try:
            name = input('이름을 입력하세요 : ')
            age = int(input('나이를 입력하세요 : '))
            self.user_data = {'이름': name, '나이': age}
        except ValueError:
            print('나이는 숫자로 입력하셔야 합니다.')

    def display_user_info(self):
        if self.user_data:
            print('사용자 정보 : ')
            for key in self.user_data:
                print(f'{key}: {self.user_data[key]}')
        else:
            print('사용자 정보가 입력되지 않았습니다.')


user = UserInfo()
# user.get_user_info()
# user.display_user_info()

# 집가서 이름도 입력이 안되거나 이상한 이름이면 
# 예외처리 하는거 한번 해보자