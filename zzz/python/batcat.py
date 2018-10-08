#!/usr/bin/env python3
# coding: utf-8
 
import os

def cat(fromfile, tofile):
    with open(fromfile, encoding="utf-8") as ff:
        filetext = ff.readlines()
    with open(tofile, "a") as tf:
        for i, line in enumerate(filetext):
                tf.write(str(i+1) + ' ' + line)
            tofile.write("================\n")

def f(dirs, newfile):
    filelist = os.listdir(dirs)
    for filename in filelist:
        filetodo = os.path.join(dirs, filename)
        if os.path.isfile(filetodo):
            if os.path.splitext(filetodo)[-1] in [".py"]:
                with open(newfile, 'a') as nf:
                    nf.wirte(filename + '\n')
                cat(filetodo, newfile)
        elif os.path.isdir(filetodo):
            f(filetodo, newfile)

cwd = os.getcwd()
p = input("path to be cat: ")
p = os.path.join(cwd, p)
fi = os.path.join(cwd, p) + ".txt"
f(d, fi)
print(d, fi)

