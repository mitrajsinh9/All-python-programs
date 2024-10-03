import time
c1= time.localtime(time.time())

h=c1.tm_hour
m=c1.tm_min
s=c1.tm_sec

if h<12:
    print(h,":",m,":",s,"good morning")
elif h>12 and h<16:
    print(h,":",m,":",s,"good afternoon")
elif h>16 and h<19:
    print(h,":",m,":",s,"good evening")
else:
    print(h,":",m,":",s,"good night")

