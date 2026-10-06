import re

text = "a123b"

if re.fullmatch(r"a.*b", text):
    print("Match")
else:
    print("No match")