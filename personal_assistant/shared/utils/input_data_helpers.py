import re

def parse_input(user_input: str) -> tuple[str, dict]:
    parsed_params = {}
    input_pattern = r"\w+=[\"\']{1}.+[\"\']{1}"
    params = re.findall(input_pattern, user_input)

    for param in params:
        key, val = param.split("=", 1)
        parsed_params[key.strip().lower()] = val.strip().strip("\"'")

    command = user_input.split()[0]

    print(command, parsed_params)

    return (command, parsed_params)



