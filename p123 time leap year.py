import time
current = time.localtime(time.time())

print("Year:", current.tm_year)

i=current.tm_year
if i%4==0:
    print("year is not leap year")
else:
    print("year is leap year")

