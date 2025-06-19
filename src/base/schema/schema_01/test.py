import os
import sys

default_variable_value = os.getenv("AIRFLOW_HOME", None)
if default_variable_value is None:
    default_variable_value = os.getenv("AIRFLOW_HOME", "/opt/airflow")

print(f"{default_variable_value=}")
print(sys.path)

# Add Common Library
add_path = os.path.dirname(os.path.abspath(__file__))
stripped_path = add_path
for _ in range(3):
    stripped_path = os.path.dirname(stripped_path)
sys.path.insert(0, stripped_path)
print(f"{stripped_path=}")

print(f"{stripped_path=}")
print(f"{sys.path=}")
from common.common_init import SetBasePath

# from common.common_init import SetBasePath

if __name__ == "__main__":
    current_directory = SetBasePath()
    print(f"{current_directory=}")
