#!/usr/bin/env python3

import os
import shutil

d = "bbb"
dirlist = os.listdir(d)
dirlist.sort()
for subdir in dirlist:
    realdir = os.path.join(d, subdir)
    if os.path.isdir(realdir):
        filelist = os.listdir(realdir)
        filelist.sort()
        for i, filename in enumerate(filelist):
            ext = os.path.splitext(filename)[-1]
            newname = "{:02d}-{:02d}{}".format(int(subdir), i+1, ext)
            oldfile = os.path.join(realdir, filename)
            newfile = os.path.join(d, newname)
            shutil.move(oldfile, newfile)
