from datetime import datetime as dt

now = dt.now()

print(now.year, now.month, now.day, sep='-')

from datetime import datetime as dt

print(str(dt.now())[:10])