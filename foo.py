#!/usr/bin/env python
import time

def f1():
    for i in range(10):
        print(i)
        time.sleep(2)
    print(i+1)

def f2():
    for a in range(1, 10):
        for b in range(1, 10):
            for c in range(1, 10):
                for d in range(1, 10):
                    for e in range(1, 10):
                        for f in range(1, 10):
                            for g in range(1, 10):
                                for h in range(1, 10):
                                    for i in range(1, 10):
                                        if len(set([a,b,c,d,e,f,g,h,i])) == 9 and a + b + c == d+e+f == g+h+i == a+d+g == b+e+h == c+f+i == a+e+i==c+e+g :
                                            print(a,b,c)
                                            print(d,e,f)
                                            print(g,h,i)
                                            print()

def f3():
    l=list(range(1,10))
    for a in l:
        la=l.copy()
        la.pop(la.index(a))
        for b in la:
            lb=la.copy()
            lb.pop(lb.index(b))
            for c in lb:
                lc=lb.copy()
                lc.pop(lc.index(c))
                for d in lc:
                    ld=lc.copy()
                    ld.pop(ld.index(d))
                    for e in ld:
                        le=ld.copy()
                        le.pop(le.index(e))
                        for f in le:
                            lf=le.copy()
                            lf.pop(lf.index(f))
                            for g in lf:
                                lg=lf.copy()
                                lg.pop(lg.index(g))
                                for h in lg:
                                    lh=lg.copy()
                                    lh.pop(lh.index(h))
                                    for i in lh:
                                        if a+b+c == d+e+f == g+h+i == a+d+g == b+e+h == c+f+i == a+e+i == c+e+g:
                                            print(a,b,c)
                                            print(d,e,f)
                                            print(g,h,i)
                                            print()
                                        

if __name__ == "__main__":
    f3()
