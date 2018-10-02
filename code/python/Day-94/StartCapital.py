import re
separated_str = re.sub("([A-Z])", " \\1", "AReallyLongVariableNameInJava").strip()
print(separated_str)
