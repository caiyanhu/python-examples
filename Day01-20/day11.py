s1 = "'hello, world!'"
s2 = "\\hello, world!\\"
print(s1)
print(s2)

s1 = "\it \is \time \to \read \now"
s2 = r"\it \is \time \to \read \now"
print(s1)
print(s2)

s1 = "\141\142\143\x61\x62\x63"
s2 = "\u9a86\u660a"
print(s1)
print(s2)

s1 = "hello" + "," + "world"
print(s1)
s2 = "!" * 3
print(s2)
s1 += s2
print(s1)
s1 *= 2
print(s1)

s1 = "hello,world"
s2 = "goodbye, world"
print("wo" in s1)
print("wo" not in s2)
print(s2 in s1)

s = "hello, world"
print(len(s))
print(len("goodbye, world!"))

s = "hello"
for i in s:
    print(i)

s1 = "hello,world"
print(s1.capitalize())
print(s1.title())
print(s1.upper())
s2 = "GOODBYE"
print(s2.lower())
print(s1)
print(s2)

s = "hello, world"
print(s.find("or"))
print(s.find("or", 9))
print(s.find("of"))
print(s.index("or"))

print(s.find("o"))
print(s.rfind("o"))
print(s.rindex("o"))

s1 = "hello,world"
print(s1.startswith("HE"))
print(s1.startswith("hel"))
print(s1.endswith("!"))
s2 = "abc123"
print(s2.isalnum())
print(s2.isdigit())
print(s2.isalpha())

s = "hello, world"
print(s.center(19, "*"))
print(s.rjust(20))
print(s.ljust(20, "~"))
print("33".zfill(5))
print("-33".zfill(5))

a = 321
b = 123
print(f"{a} * {b} = {a * b}")

s1 = "   jackfrued@126.com  "
print(s1.strip())
s2 = "~你好，世界~"
print(s2.lstrip("~"))
print(s2.rstrip("~"))

s = "hello, good world"
print(s.replace("o", "@"))
print(s.replace("o", "@", 1))

s = "I love you"
print(s.split())
print("~".join(s.split()))

s = "I#love#you#so#much"
words = s.split("#")
print(words)
words = s.split("#", 2)
print(words)

a = "骆昊"
b = a.encode("utf-8")
c = a.encode("gbk")
print(b)
print(c)
print(b.decode("utf-8"))
print(c.decode("gbk"))
