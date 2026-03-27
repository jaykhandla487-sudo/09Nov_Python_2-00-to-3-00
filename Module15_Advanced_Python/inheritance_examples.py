class Person:

    def show(self):
        print("This is parent class")

class Student(Person):

    def display(self):
        print("This is child class")

s = Student()

s.show()
s.display()