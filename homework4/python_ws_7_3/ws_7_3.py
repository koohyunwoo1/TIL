# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    

    def calculate_perimeter(self):
        return 2 * (self.x + self.y)


shape1 = Shape(5, 3)
perimeter1 = shape1.calculate_perimeter()
print(perimeter1)
