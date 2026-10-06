import re

txt = "Åland"

#Find all UNICODE matches:
print(re.findall("\w", txt, re.UNICODE))


#Same result using the shorthand re.U flag:
print(re.findall("\w", txt, re.U))