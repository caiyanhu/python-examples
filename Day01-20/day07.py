import random

"""
输出100以内的素数
"""

for num in range(2, 100):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

"""
找出100到999范围内的水仙花数
"""
for num in range(100, 1000):
    low = num % 10
    middle = num // 10 % 10
    high = num // 100
    if num == high**3 + middle**3 + low**3:
        print(num)

"""
百钱百鸡问题
"""
for x in range(0, 21):
    for y in range(0, 34):
        z = 100 - x - y
        if z % 3 == 0 and 5 * x + 3 * y + z // 3 == 100:
            print(f"公鸡: {x}只, 母鸡: {y}只, 小鸡: {z}只")

"""
Craps赌博游戏
"""

money = 1000
while money > 0:
    print(f"你的总资产为:{money}元")
    while True:
        debt = int(input("请下注:"))
        if 0 < debt < money:
            break
    first = random.randrange(1, 7) + random.randrange(1, 7)
    print(f"\n玩家摇出了{first}点")

    if first == 7 or first == 11:
        money += debt
        print("玩家胜\n")
    elif first == 2 or first == 3 or first == 12:
        money -= debt
        print("庄家胜\n")
    else:
        while True:
            current = random.randrange(1, 7) + random.randrange(1, 7)
            print(f"\n玩家摇出了{current}点")
            if current == 7:
                money -= debt
                print("庄家胜\n")
                break
            elif current == first:
                money += debt
                print("玩家胜\n")
                break

print("你破产了,游戏结束!")
