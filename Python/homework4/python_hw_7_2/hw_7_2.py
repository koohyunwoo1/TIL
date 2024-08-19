# 아래 클래스를 수정하시오.
class StringRepeater:
    def repeat_string(self,x,y):
        for i in range(x):
            print(y)


repeater1 = StringRepeater()  
result = repeater1.repeat_string(3, "Hello")