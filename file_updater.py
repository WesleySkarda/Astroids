import re

def update_file(filepath, updated_vars: dict):
    with open(filepath, 'r') as file:
        content = file.read()

    for var, new_value in updates.items():
        content = re.sub(rf"^{var}\s*=.*$", f"{var} = {new_value}", content, flags=re.MULTILINE)
    
    with open(filepath, "w") as file:
        file.write(content)