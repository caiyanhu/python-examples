import random

languages = ["Python", "Java", "C++"]
languages.append("JavaScript")
print(languages)

languages.insert(1, "SQL")
print(languages)

if "Java" in languages:
    languages.remove("Java")
if "Swift" in languages:
    languages.remove("Swift")
print(languages)
languages.pop()
temp = languages.pop(1)
print(temp)
languages.append(temp)
print(languages)
languages.clear()
print(languages)

items = ["Python", "Java", "C++"]
del items[1]
print(items)

items = ["Python", "Java", "Java", "C++", "Kotlin", "Python"]
print(items.index("Python"))
print(items.index("Python", 1))
print(items.count("Python"))
print(items.count("Kotlin"))
print(items.count("Swift"))
# print(items.index("Java", 3))

items = ["Python", "Java", "C++", "Kotlin", "Swift"]
items.sort()
print(items)
items.reverse()
print(items)

items = [i for i in range(100) if i % 3 == 0 or i % 5 == 0]
print(items)

nums1 = [35, 12, 97, 64, 55]
nums2 = [num**2 for num in nums1]
print(nums2)

nums1 = [35, 12, 97, 64, 55]
nums2 = [num for num in nums1 if num > 50]
print(nums2)

scores = [[random.randrange(60, 100) for _ in range(3)] for _ in range(5)]
print(scores)

red_balls = [i for i in range(34)]
blue_balls = [i for i in range(17)]
selected_balls = random.sample(red_balls, 6)
selected_balls.sort()
for ball in selected_balls:
    print(f"\033[031m{ball:0>2d}\033[0m", end=" ")
blue_ball = random.choice(blue_balls)
print(f"\033[034m{blue_ball:0>2d}\033[0m")
