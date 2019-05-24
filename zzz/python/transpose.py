#!/data/data/com.termux/files/usr/bin/env python3

with open("poet") as poet:
    pl = poet.readlines()

new = zip(*pl)
new = [''.join(reversed(i)) + '\n' for i in new]
new.pop()

with open("newpoet", 'w') as f:
    f.writelines(new)
