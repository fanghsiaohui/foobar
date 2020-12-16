import time
def f(n):
    if n==0:
        return 1
    else:
        return n*f(n-1)

if __name__ == "__main__":
    for i in range(800):
        t = time.perf_counter()
        print(i, f(i))
        print("time:", time.perf_counter() - t)
