dt = {"a": "juice", "b": "grill", "c": "corn"}
# using items()
for key, value in dt.items():
    print(key, value)

# without using items
for key in dt:
    print(key, dt[key])

# return keys and values explicitly
for key in dt.keys():
    print(key)
for value in dt.values():
    print(value)
