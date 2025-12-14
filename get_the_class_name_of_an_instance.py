class Vehicle:
    def name(self, name):
        return name


v = Vehicle()
print(v.__class__.__name__)


class Car:
    def name(self, name):
        return name


c = Car()
print(type(c).__name__)
