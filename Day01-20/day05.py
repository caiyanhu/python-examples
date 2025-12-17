"""
BMI计算器
"""

height = float(input("身高(cm)："))
weight = float(input("体重(kg)："))
bmi = weight / (height / 100) ** 2
print(f"{bmi = :.1f}")
match bmi:
    case bmi if bmi < 18.5:
        print("你的体重过轻！")
    case bmi if bmi < 24:
        print("你的身材很棒！")
    case bmi if bmi < 27:
        print("你的体重过重！")
    case bmi if bmi < 30:
        print("你已轻度肥胖！")
    case bmi if bmi < 35:
        print("你已中度肥胖！")
    case _:
        print("你已重度肥胖！")

"""
分段函数求值
"""
x = float(input("x = "))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print(f"{y = }")

"""
百分制成绩转换为等级制成绩
"""
score = float(input("请输入成绩: "))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "E"
print(f"{grade = }")

"""
计算三角形的周长和面积
"""
print("请三角形各边长")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if a + b > c and a + c > b and b + c > a:
    perimeter = a + b + c
    print(f"周长: {perimeter}")
    s = perimeter / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print(f"面积: {area}")
else:
    print("不能构成三角形")
