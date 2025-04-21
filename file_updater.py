import re
from constants import *

def update_file(file_path, updates: dict):
    #call function with a dictonary that has the varable name as a string and the updated value as its value
    # such as update_file("constraints.py", {"SCREEN_WIDTH": 1920})

    with open(file_path, "r") as file:
        content = file.read()


    # Update variables using regex
    for var, new_value in updates.items():
        pattern = rf"^{var}\s*=\s*.+$"
        replacement = f"{var} = {new_value}"
        content = re.sub(pattern, replacement, content, flags=re.MULTILINE)

    # Save the updated content back to the file
    with open(file_path, "w") as file:
        file.write(content)
