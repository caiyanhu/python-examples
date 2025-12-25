class Student:
    __slots__ = ("name", "age")

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def study(self, course_name):
        print(f"{self.name}正在学习{course_name}")


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and a + c > b and b + c > a

    @property
    def perimeter(self):
        return self.a + self.b + self.c

    @property
    def area(self):
        p = self.perimeter / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


triangle = Triangle(3, 4, 5)
print(triangle.area)
print(triangle.perimeter)
print(triangle.is_valid(3, 4, 5))
print(Triangle.is_valid(3, 4, 5))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name}正在吃饭")

    def sleep(self):
        print(f"{self.name}正在睡觉")


class Stu(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def study(self, course_name):
        print(f"{self.name}正在学习{course_name}")


class Teacher(Person):
    def __init__(self, name, age, title):
        super().__init__(name, age)
        self.title = title

    def teach(self, course_name):
        print(f"{self.name}{self.title}正在讲授{course_name}")


student1 = Stu("白元芳", 21)
student2 = Stu("狄仁杰", 22)
teacher1 = Teacher("武则天", 35, "副教授")
student1.eat()
student2.sleep()
teacher1.eat()
student1.study("Python程序设计")
teacher1.teach("Python程序设计")
