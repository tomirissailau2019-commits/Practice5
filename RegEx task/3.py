import re

text = "hello_world test hello_world123"

result = re.findall(r"\b[a-z]+_[a-z]+\b", text)

print(result)