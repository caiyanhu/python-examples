index = [1, 2, 3]
languages = ["python", "c", "c++"]

dictionary = dict(zip(languages, index))
print(dictionary)

another_dict = {k: v for k, v in zip(index, languages)}
print(another_dict)
