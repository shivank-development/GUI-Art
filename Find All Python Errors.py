import re
import builtins

for i in dir(builtins):
    if re.match(r'^[A-Z]', i):
        print(i)
