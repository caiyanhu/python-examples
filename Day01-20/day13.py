person = {
    "name": "王大锤",
    "age": 55,
    "height": 168,
    "weight": 60,
    "addr": "成都市武侯区科华北路62号1栋101",
    "tel": "13122334455",
    "emergence contact": "13800998877",
}
print(person)

# dict函数(构造器)中的每一组参数就是字典中的一组键值对
person = dict(
    name="王大锤", age=55, height=168, weight=60, addr="成都市武侯区科华北路62号1栋101"
)
print(person)

# 可以通过Python内置函数zip压缩两个序列并创建字典
item1 = dict(zip("ABCDE", "12345"))
print(item1)
item2 = dict(zip("ABCDE", range(1, 10)))
print(item2)

# 用字典生成式语法创建字典
item3 = {x: x**3 for x in range(1, 6)}
print(item3)

# 成员运算
print("name" in person)
print("tel" in person)

# 索引运算
print(person["name"])
print(person["addr"])
person["age"] = 25
person["height"] = 180
person["tel"] = "13122334455"
person["signature"] = "你的男朋友是一个盖世垃圾，他会踏着五彩祥云去迎娶你的闺蜜"
print(person)
for key in person:
    print(f"{key}:\t{person[key]}")

# 字典方法
person = {
    "name": "王大锤",
    "age": 25,
    "height": 178,
    "addr": "成都市武侯区科华北路62号1栋101",
}
print(person.get("name"))
print(person.get("sex"))
print(person.get("sex", True))

person = {"name": "王大锤", "age": 25, "height": 178}
print(person.keys())
print(person.values())
print(person.items())
for key, value in person.items():
    print(f"{key}:\t{value}")

person1 = {"name": "王大锤", "age": 55, "height": 178}
person2 = {"age": 25, "addr": "成都市武侯区科华北路62号1栋101"}
person1.update(person2)
print(person1)


person = {
    "name": "王大锤",
    "age": 25,
    "height": 178,
    "addr": "成都市武侯区科华北路62号1栋101",
}
print(person.pop("age"))
print(person)
print(person.popitem())
print(person)
person.clear()
print(person)

sentence = input("请输入一段话:")
counter = {}
for ch in sentence:
    if "A" <= ch <= "Z" or "a" <= ch <= "z":
        counter[ch] = counter.get(ch, 0) + 1

sorted_keys = sorted(counter, key=counter.get, reverse=True)
for key in sorted_keys:
    print(f"{key}出现了 {counter.get(key)}次")

stocks = {
    "AAPL": 191.88,
    "GOOG": 1186.96,
    "IBM": 149.24,
    "ORCL": 48.44,
    "ACN": 166.89,
    "FB": 208.09,
    "SYMC": 21.29,
}
stocks2 = {key: value for key, value in stocks.items() if value >= 100}
print(stocks2)
