import datetime as dt

myBirthDay = dt.datetime(2007, 11, 12)
print(myBirthDay)

now = dt.datetime.now()
print(now)

import re

text = "The rain in a spain 14020@"

print(re.search(r"\AThe", text)) #['ai', 'ai']
print(re.search("ai", text)) # <re.Match object; span=(5, 7), match='ai'>
print(re.split("ai", text)) # ['The r', 'n in a sp', 'n']
print(re.sub("ai", "die", text)) # The rdien in a spdien