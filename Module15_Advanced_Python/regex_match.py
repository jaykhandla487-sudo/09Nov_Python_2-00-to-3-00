import re

text = "Python"

result = re.match("Py", text)

if result:
    print("Match at beginning")
else:
    print("No match")