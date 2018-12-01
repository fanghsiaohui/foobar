#!/usr/bin/python3
# import pdb, sys, re, time, os, shutil, command
# pdb.set_trace()
# from functools import wraps
# print(*(enumerate(range(10))))

import tkinter
def func():
    pass

def test():
    win = tkinter.Tk()
    win.title("tk title")
    win.geometry("900x600")
    btn = tkinter.Button(win, text = "tk btn", command = func())
    btn.pack(expand = 1, fill = "y")
    tkinter.mainloop()

if __name__ == "__main__":
    test()
