import time


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print(f"{self.name}正在学习{course_name}")

    def play(self):
        print(f"{self.name}正在玩游戏")


student1 = Student("骆昊", 44)
student2 = Student("王大锤", 25)

print(student1)
print(student2)
print(hex(id(student1)), hex(id(student2)))

student1.study("Python程序设计")

student2.play()


class Clock:
    def __init__(self, hour=0, minute=0, second=0):
        """初始化方法
        :param hour: 时
        :param minute: 分
        :param second: 秒
        """
        self.hour = hour
        self.min = minute
        self.sec = second

    def run(self):
        self.sec += 1
        if self.sec == 60:
            self.sec = 0
            self.min += 1
            if self.min == 60:
                self.min = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0

    def show(self):
        return f"{self.hour:0>2d}:{self.min:0>2d}:{self.sec:0>2d}"


clock = Clock(23, 59, 58)


class Point:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

    def distance_to(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx * dx + dy * dy) ** 0.5

    def __str__(self) -> str:
        return f"({self.x},{self.y})"


p1 = Point(3, 5)
p2 = Point(6, 9)
print(p1)
print(p2)
print(p1.distance_to(p2))
