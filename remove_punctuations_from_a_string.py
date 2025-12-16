# define punctuation
punctuations = """!()-[]{};:'"\\,<>./?@#$%^&*_~"""


my_str = "Hello!!!, he said ---and went."

no_puct = ""
for char in my_str:
    if char not in punctuations:
        no_puct = no_puct + char

print(no_puct)
