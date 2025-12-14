import os
import pathlib

file_details = os.path.splitext("./data_file.txt")
print(file_details)
print(file_details[1])

print(pathlib.Path("./data_file.txt").suffix)
