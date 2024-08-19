'''
    framework를 사용한다는 것은 어쩔 수 없는 부분이 있다.
    그래서 매번 강조하는 내용은 DOCS 보세요.
    django만 해당하는게 아니라... 모든 곳에서 다 동일한 이야기.
    회사가서 일해도 똑같아요
'''
from django.views.decorators.http import require_http_methods

'''
@login_required
def index(request):
    pass
'''

class Person:
    @classmethod
    def class_function(cls):
        pass

    @staticmethod
    def static_function():
        pass

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(args)
        print('여기가 데코레이터가 하는 일')
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def my_function(a, b):
    return a + b

my_function(1, 3)

def login_required(view_func):
    def wrapper(*args, **kwargs):
        request, args = args
        if request.user.is_authenticated:
            return view_func(request, args)
        return redirect('accounts:login')
    return wrapper

@login_required
def index(request):
    return ...

# index view함수 호출시...
index()

'''
def require_http_methods(view_func):
    def wrapper(*args, **kwargs):
        request, methods, args = args
        if request.method in methods:
            return view_func()
        return ...?

'''

@require_http_methods(['GET', 'POST'])
def index(request):
    pass