#!/usr/bin/env python3
# coding: utf-8
 
# import pdb
# pdb.set_trace()
# import sys, re, time, os, shutil, command
# from functools import wraps

import os

def cat(fromfile, tofile):
    with open(fromfile) as fromfile:
        with open(tofile, "a") as tofile:
            for i, line in enumerate(fromfile.readlines()):
                tofile.write(str(i+1) + ' ' + line)
            tofile.write("================\n")

def f(dirs, newfile):
    filelist = os.listdir(dirs)
    for fd in filelist:
        filetodo = os.path.join(dirs, fd)
        bbb =  os.path.isfile(filetodo)
        if os.path.isfile(filetodo):
            # if os.path.splitext(filetodo)[-1] in [".py", ".txt"]:
            if os.path.splitext(filetodo)[-1] in [".py"]:
                # 写入文件名，并关闭文件
                filenew = open(newfile, 'a')
                filenew.write(fd + "\n")
                filenew.close()
                # with open(newfile, 'a') as nf:
                    # nf.write(fd)

                cat(filetodo, newfile)
        elif os.path.isdir(filetodo):
            f(filetodo, newfile)


cwd = os.getcwd()
# d = "python"
d = input("path to be cat: ")
d = os.path.join(cwd, d)
# fi = "newfile"
fi = d + ".txt"
fi = os.path.join(cwd, fi)
f(d, fi)
print(d,fi)

