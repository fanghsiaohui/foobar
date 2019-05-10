#!/usr/bin/python3
import tkinter

def func():
    print("hello, sb")

def test():
    win = tkinter.Tk()
    win.title("tk title")
    win.geometry("900x600")
    btn = tkinter.Button(win, text = "click me", command = func)
    btn.pack(expand = 1, fill = "y")
    tkinter.mainloop()

if __name__ == "__main__":
    test()
