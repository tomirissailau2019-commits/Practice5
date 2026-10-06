import re

text = "abbb"

if re.fullmatch(r"ab*", text):
    print("Match")
else:
    print("No match")