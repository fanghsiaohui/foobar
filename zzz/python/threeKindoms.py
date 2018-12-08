#!/usr/bin/env python3

import jieba

txt = open("threekingdoms.txt", "r", encoding = "utf-8").read()
excludes = {"", "", "", "", ""}
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "" or word == "":
        rword = ""
    elif word == "" or word == "":
        rword = ""
    elif word == "" or word == "":
        rword = ""
    elif word == "" or word == "":
        rword = ""
    elif word == "" or word == "":
        rword = ""
    elif word == "" or word == "":
        rword = ""
    else:
        rword = word
    counts[rword] = counts.get(rword, 0) + 1
for word in excludes:
    del counts[word]
items = list(counts.items())
items.sort(key = lambda x:x[1], reverse = True)
for i in range(10):
    word, count = items[i]
    print("{0:<10}: {1:>5}".format(word, count))

