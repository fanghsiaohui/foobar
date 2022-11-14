#!/usr/bin/python3

import zipfile

f = zipfile.ZipFile('foo.zip')

with open('dict5m') as d:
    for line in d:
        try:
            f.extractall(pwd=bytes(line.strip(), 'utf8'))
            print('password is {0}'.format(line.strip()))
            break
        except:
            pass
