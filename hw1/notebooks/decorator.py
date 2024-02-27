# 데코레이터로 사용할 함수 (인자 : 함수)
def my_decorator(func):
    def wrapper():
        print('인자로 받은 func 호출되기 전에 할일')
        func()
        print('인자로 받은 func 호출되고 나서 할일')
    return wrapper

@my_decorator
def greeting():
    print('안녕~')

greeting()