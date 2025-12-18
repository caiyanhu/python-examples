import timeit

# 定义一个三元组
t1 = (35, 12, 98)
# 定义一个四元组
t2 = ("骆昊", 45, True, "四川成都")

print(type(t1))
print(type(t2))
print(len(t1))
print(len(t2))
print(t1[0])
print(t1[1])
print(t2[-1])

print(t2[:2])
print(t2[::3])

print(12 in t1)
print(99 in t1)
print("CC" not in t2)

t3 = t1 + t2
print(t3)

print(t1 == t3)
print(t1 >= t3)

a = ()
print(type(a))
b = "hello"
print(type(b))
c = 100
print(type(c))
d = ("hello",)
print(type(d))
e = (100,)
print(type(e))

# pack unpack
a = 1, 10, 100, 1000
print(type(a))
i, j, *k = a
print(i, j, k)
i, *j, k = a
print(i, j, k)
*i, j, k = a
print(i, j, k)
*i, j = a
print(i, j)
i, j, k, *l = a
print(i, j, k, l)
i, j, k, l, *m = a
print(i, j, k, l, m)

print("%.3f 秒" % timeit.timeit("[1, 2, 3, 4, 5, 6, 7, 8, 9]", number=100000000))
print("%.3f 秒" % timeit.timeit("(1, 2, 3, 4, 5, 6, 7, 8, 9)", number=100000000))

infos = ("骆昊", 43, True, "四川成都")
print(list(infos))

frts = ["apple", "banana", "orange"]
print(tuple(frts))
# 将元组转换成列表
