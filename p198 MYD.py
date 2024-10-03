import time
c1 = time.localtime(time.time())

m=c1.tm_mon
y=c1.tm_year
d=c1.tm_mday

print(d,"/",m,"/",y)