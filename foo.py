import time, sys
try:
    i = int(sys.argv[1])
except:
    i = 3

def test():
    return 0

while i>0:
    print(i)
    if test():
        break
    time.sleep(1)
    i -= 1
else:
    print("0:\tfire")

