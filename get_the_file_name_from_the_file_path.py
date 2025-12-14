import os
from pathlib import Path

# file name with extension
file_name = os.path.basename("./data_file.txt")
print(file_name)
# ile name without extension
print(os.path.splitext(file_name)[0])

print(Path("./data_file.txt").stem)
