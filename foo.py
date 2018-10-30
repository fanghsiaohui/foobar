#!/usr/bin/env python3
 
# import pdb
# pdb.set_trace()
# import sys, re, time, os, shutil, command
# from functools import wraps
# print(*(enumerate(range(10))))

__metaclass__ = type

class Person():
    def setName(self, name):
        self.__name__ = name
    def getName(self):
        return self.__name__
    def greet(self):
        print("hello, world! I'm %s." % self.__name__)

class Bird:
    song = "bugu!"
    def sing(self):
        print(self.song)

class Secretive:
    def __inaccessible(self):
        print("you cannot see me...")
    def accessible(self):
        print("the secret message is: ")
        self.__inaccessible()

