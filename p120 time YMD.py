import time
current = time.localtime(time.time())

print("Year:", current.tm_year)
print("Month:", current.tm_mon)
print("Day:", current.tm_mday)

d=current.tm_mday
m=current.tm_mon
y=current.tm_year

print(d,"/",m,"/",y)
