import time
import sys
def f(n):
    if n==0:
        return 1
    else:
        return n*f(n-1)

if __name__ == "__main__":
    try:
        n=int(sys.argv[1])
    except:
        n=10
    for i in range(n+1):
        t = time.perf_counter()
        print(i, f(i))
        print("time:", time.perf_counter() - t)
