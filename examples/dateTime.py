import time;

localtime = time.asctime(time.localtime(time.time()))
print "Local current time :", localtime

hr= int(localtime[11:13])

if hr>=5 and hr<12:
    print "Good Morning"
if hr>=12 and hr<15:
    print "Good Noon"
if hr>=15 and hr<18:
    print "Good Afternoon"
if hr>=18 and hr<20:
    print "good Evening"
if hr>=20 and hr<23:
    print "Good Night"
if hr>=0 and hr<5:
    print "Good Night"