# 아래 클래스를 수정하시오.

class Animal:
    num_of_animal = 0

    def __init__(self):
        Animal.num_of_animal += 1
        print(f'동물의 수는 {Animal.num_of_animal}마리 입니다.')
        

class Dog(Animal):
   pass


class Cat(Animal):
    pass


class Pet(Dog, Cat):
    @classmethod
    def access_num_of_animal(self):
        return Animal.num_of_animal


dog = Dog()
# print(Pet.access_num_of_animal())
cat = Cat()
# print(Pet.access_num_of_animal())







# class Animal:
#     num_of_animal = 0
        

# class Dog(Animal):

#     def __init__(self):
#         super().num_of_animal += 1


# class Cat(Animal):
#     def __init__(self):
#         super().num_of_animal += 1
    


# class Pet(Dog, Cat):

#     @classmethod
#     def access_num_of_animal(cls):
#         return f'동물의 수는 {cls.num_of_animal}마리 입니다.


# dog = Dog()
# print(Pet.access_num_of_animal())
# cat = Cat()
# print(Pet.access_num_of_animal())