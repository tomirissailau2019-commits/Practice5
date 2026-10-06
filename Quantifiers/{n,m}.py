import re

text = "Values: 1 12 123 1234 12345"
pattern = r"\d{2,4}"

print(re.findall(pattern, text))  # ['12', '123', '1234']
