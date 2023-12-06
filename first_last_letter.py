import re

text = """
kjjkdjfd madam kjjkdjfd
jksjdk@abc@345jk 1abc1 fdskj
!ok! @abc@
a434#)43a
"""
l = text.split()
pattern = r'^(.)(.+)\1$'
for t in l:
    words = re.search(pattern, t)
    if words:
        print(words.group())
