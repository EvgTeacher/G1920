class Student:
    education = 'STEP'
    group = 1920
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        print('Создался объект')



st1 = Student(name='Anna', age=17, height=175)
st2 = Student(name='Igor', age=19, height=180)
print(st1.name)
print(st2.name)
print(st1.height)
print(st2.height)
# print(id(st1))

# print(st1.education)
# print(Student.education)
# print(st1.name)
# # print(Student.name)
# print(st1.height)
# st2 = Student()
# # print(id(st2))
# print(st2.education)
# print(st2.age)