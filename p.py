import time, sys
try:
    i = int(sys.argv[1])
except:
    i = 3

while i>0:
    print(i)
    time.sleep(1)
    i -= 1
else:
    print("0:\tfire")
