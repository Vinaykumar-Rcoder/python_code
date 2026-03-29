# class Student:
#      def __init__(self, name, grade):
#          self.name = name
#          self.grade = grade
#      def car(self, model, color):
#          self.model = model
#          self.color = color
#      def drawing(self, size, colors):
#          self.size = size
#          self.colors = colors
# student1 = Student("Ravi","BA")
# student1.car("bs6", "Red")
# student1.drawing(15,"blue with black")
# print(student1.grade)
# print(student1.model)
# print(student1.color)
# print(student1.name)
# print(student1.size)
# print(student1.colors)
# ### 1. Abstraction
# ### 2..Encapsulation (oops) in python
# ## hide feacture 
# # 
# class Student:
#      def __init__(self, name, grade):
#          self.name = name
#          self.grade = grade
#      def car(self, model, color):
#          self.model = model
#          self.color = color
#      def drawing(self, size, colors):
#          self.size = size
#          self.__colors = colors
#      def student_detail(self):
#          print(f'{self.name} is in class {self.grade}')
#      def get_grade(self):
#          return self.__grade
#      def get_colors(self):
#          return self.__colors
# student1 = Student("Ravi","BA")
# student1.car("bs6", "Red")
# student1.drawing(15,"blue with black")
# print(student1.get_grade())
# print(student1.model)
# print(student1.color)
# print(student1.name)
# print(student1.size)
# print(student1.get_colors())
# s1 = Student("Raviraj", 12)
# s2 = Student("Ravi prashad", 11)
# (s1.student_detail())
# (s2.student_detail())
# ## 3.. Inheritance(oops) in pytho
# ## Baap Beta bala concept
 
# ## 4. Polymorphism (oops)

# class Student:
#      def __init__(self, name, grade):
#          self.name = name
#          self.grade = grade
#      def student_detail(self):
#          print(f'{self.name} is in class {self.grade}')
# class Gradstudent:
#      def __init__ (self, name, grade, percentage):
#          self.name = name
#          self.grade = grade
#          self.percentage = percentage
#      def student_detail(self):
#          print(f'{self.name} is in class {self.grade} with percentage : {self.percentage}%')
# s1 = Student("madhav", 12)
# s2 = Gradstudent("Manav", 11, 98)
# s1.student_detail()
# s2.student_detail()




# ===============================
# 1. Encapsulation + Abstraction
# ===============================
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.__grade = grade      # private variable
        self.model = None
        self.color = None
        self.size = None
        self.__colors = None      # private variable

    # public method
    def car(self, model, color):
        self.model = model
        self.color = color

    # abstraction (user ko detail nahi pata)
    def drawing(self, size, colors):
        self.size = size
        self.__colors = colors

    def student_detail(self):
        print(f'{self.name} is in class {self.__grade}')

    # getter methods (encapsulation)
    def get_grade(self):
        return self.__grade

    def get_colors(self):
        return self.__colors


# object create
s1 = Student("Ravi", "BA")
s1.car("BS6", "Red")
s1.drawing(15, "Blue with Black")

print(s1.get_grade())
print(s1.name)
print(s1.model)
print(s1.color)
print(s1.size)
print(s1.get_colors())

s1.student_detail()


# ===============================
# 2. Inheritance (Baap-Beta concept)
# ===============================

class GradStudent(Student):   # inheritance
    def __init__(self, name, grade, percentage):
        super().__init__(name, grade)
        self.percentage = percentage

    # method override (polymorphism bhi)
    def student_detail(self):
        print(f'{self.name} is in class {self.get_grade()} with percentage {self.percentage}%')


s2 = GradStudent("Manav", 11, 98)
s2.student_detail()


# ===============================
# 3. Polymorphism
# ===============================

students = [
    Student("Raviraj", 12),
    GradStudent("Ravi Prashad", 11, 85)
]

for stu in students:
    stu.student_detail()   # same method, different output