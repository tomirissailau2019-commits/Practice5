import re

text = "Hello World apple Python"

result = re.findall(r"\b[A-Z][a-z]+\b", text)

print(result)