class Car:
    # 아래에 코드를 작성하시오.
    wheels = 4
    def __init__(self,gasoline,diesel,hybrid,전륜구동,후륜구동,4wd,부릉부릉,달달달달,슈웅):
        self.gasoline = gasoline
        self.diesel = diesel
        self.hybrid = hybrid
        self.전륜구동 = 전륜구동
        self.후륜구동 = 후륜구동
        self.4wd = 4wd
        self.부릉부릉 = 부릉부릉
        self.달달달달 = 달달달달
        self.슈웅 = 슈웅
        
  

car1 = Car('gasoline', '후륜구동', '부릉부릉')
car2 = Car('diesel', '전륜구동', '달달달달')
car3 = Car('hybrid', '4wd', '슈웅')

car1.drive()
print(car2.drive())

print('===')
car1.introduce()
car3.introduce()

print('===')
print(f'이 세상의 자동차는 {Car.wheels}개의 바퀴를 가집니다.')
Car.increase_wheels()
print(f'이 세상의 자동차는 {Car.wheels}개의 바퀴를 가집니다.')
