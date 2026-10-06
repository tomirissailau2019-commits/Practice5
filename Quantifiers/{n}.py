import re

text = "ID: 12345"
pattern = r"\d{3}"

print(re.findall(pattern, text))  # ['123']
