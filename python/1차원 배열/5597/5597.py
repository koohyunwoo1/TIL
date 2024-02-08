import sys
sys.stdin = open('input.txt')

student = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for i in range(1,31):
    student[i] = i


for i in range(28):
    students = int(input())
    if students in student:
        student[students] = 0

for i in range(1,31):
    if student[i] == 0:
        pass
    else:
        print(student[i])