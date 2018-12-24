#!/usr/bin/env python3
# import pdb, sys, re, time, os, shutil, command
# from functools import wraps
# pdb.set_trace()

class Person:
    cnt = 0
    def __init__(self, name, gender="male", age=20):
        self.name = name
        self.gender = gender
        self.age = age
        Person.cnt += 1
    def show(self, end='\n'):
        print("name: {:>6},\tgender:\t{:>6},\tage: {:>2}".format(
            self.name, self.gender, self.age), end=end)

class Employee(Person):
    cnt = 0
    def __init__(self, name, gender="male", age=20,
            zw="worker", salary=3000):
        Person.__init__(self, name=name, gender=gender, age=age)
        self.zw = zw
        self.salary = salary
        Employee.cnt += 1
    def show(self):
        Person.show(self, end=',\t')
        print("zw: {:>0},\tsalary: {:>6d}".format(
            self.zw, self.salary))

zhao = Person(name="zhao")
qian = Person(name="qian", gender="female", age=18)
sun = Employee(name="sun")
li = Employee(name="li", zw="artist", salary=5000)
print("number of person: {:2d}".format(Person.cnt))
print("number of Employee: {:2d}".format(Employee.cnt))
zhao.show()
qian.show()
sun.show()
li.show()
