import re

text = "Python programming language"

result = re.search("programming", text)

if result:
    print("Match found")
else:
    print("No match")