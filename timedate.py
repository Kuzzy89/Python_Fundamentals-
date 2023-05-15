
from datetime import datetime

# current date and time
now = datetime.now()

t = now.strftime("%Y/%m/%d")
print(t)

s1 = now.strftime("%d/%m/%Y")
print(s1)
