## oops in python

# class Student:
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade

#     def car(self, model, color):
#         self.model = model
#         self.color = color

#     def drawing(self, size, colors):
#         self.size = size
#         self.colors = colors

# student1 = Student("Ravi","BA")
# student1.car("bs6", "Red")
# student1.drawing(15,"blue with black")

# print(student1.grade)
# print(student1.model)
# print(student1.color)
# print(student1.name)

# print(student1.size)
# print(student1.colors)

### 1..Encapsulation (oops) in python

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def car(self, model, color):
        self.model = model
        self.color = color

    # def drawing(self, size, colors):
    #     self.size = size
    #     self.__colors = colors

    def student_detail(self):
       print(f'{self.name} is in class {self.grade}')

    # def get_grade(self):
    #     return self.__grade
    
    # def get_colors(self):
    #     return self.__colors

    
# student1 = Student("Ravi","BA")
# student1.car("bs6", "Red")
# student1.drawing(15,"blue with black")

# print(student1.get_grade())
# print(student1.model)
# print(student1.color)
# print(student1.name)

# print(student1.size)
# print(student1.get_colors())
s1 = Student("Raviraj", 12)
s2 = Student("Ravi prashad", 11)
(s1.student_detail())
(s2.student_detail())


### 2.. Inheritance(oops) in python

