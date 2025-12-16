import os
import pathlib

file_stat = os.stat("./code_check.txt")
print(file_stat.st_size)

file = pathlib.Path("./code_check.txt")
print(file.stat().st_size)
