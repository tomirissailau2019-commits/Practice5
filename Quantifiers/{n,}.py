import re

text = "A=12, B=123, C=12345"
pattern = r"\d{3,}"

print(re.findall(pattern, text))  # ['123', '12345']