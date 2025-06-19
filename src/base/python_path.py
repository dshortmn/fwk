import os
import sys

add_path = os.path.dirname(os.path.abspath(__file__))
print(add_path)
stripped_path = add_path
# Strip 3 levels
for _ in range(3):
    stripped_path = os.path.dirname(stripped_path)
sys.path.insert(0, stripped_path + "/common")
