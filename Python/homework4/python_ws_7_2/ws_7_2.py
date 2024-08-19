# 아래 클래스를 수정하시오.
# 사각형의 넓이를 계산하여 반환하시오.
class Shape:
    def __init__(self, x, y ):
        self.x = x
        self.y = y
        
    def calculate_area(self):
        return self.x * self.y




shape1 = Shape(5, 3)
area1 = shape1.calculate_area()
print(area1)   # 15
