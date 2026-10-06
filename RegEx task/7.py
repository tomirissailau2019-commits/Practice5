text = "hello_world_python"

words = text.split("_")

result = words[0] + "".join(word.capitalize() for word in words[1:])

print(result)