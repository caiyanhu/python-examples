import os.path
import time
import pathlib

file = pathlib.Path("./access_index_of_a_list_using_for_loop.py")
print("Last modification time: %s" % time.ctime(os.path.getmtime(file)))
print(
    "Last metadata change time or path creation time: %s"
    % time.ctime(os.path.getctime(file))
)
