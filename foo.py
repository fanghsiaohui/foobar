#!/usr/bin/env python3
# coding: utf-8
# 
# import pdb
# pdb.set_trace()

# t = ('t1', 't2', 't3')
# l = ['l1', 'l2', 'l3']
# d = {'k1':'v1', 'k2':'v2', 'k3':'v3'}
# s = {'s1', 's2', 's3'}
# 
# for i in (t, l, d, s):
#     a, *b = i
#     print(i)
#     print(a, b)
# 
# a, *b = t
# print(a, b)
# 
# """七天学会Python，bilibili视频
# 
# 教学视频
# """
# 
# class Humen():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# 
# class Student(Human):
#     sum = 0
# #    def __init__(self, name, age):
# #        self.name = name
# #        self.age = age
# #        self.score = 0
#     def __init__(self, school):
#         self.school = school
# 
#     def doHomework(self):
#         print("do homework.")
# 
#     def marking(self, score):
#         if score < 0:
#             print("invalid score.")
#         self.score = score
# 
#     @classmethod
#     def plusSum(cls):
#         cls.sum += 1
#         print("num of student: ", cls.sum)
# 
#     @staticmethod
#     def add(x, y):
#         print(Student.sum)
#         print("this is a static method")
# 
# student1 = Student("zhangsan", 10)
# student2 = Student("lisi", 11)
# 
# print(student1.name + ", score:" + str(student1.score))
# print(student1.__dict__)
# print(student2.__dict__)
# print(Student.__dict__)

# import re
# a = 'asdf32dsaf42rdsf5690wusd'
# r = re.findall('[0-9]', a)
# r2 = re.findall('\d', a)
# print(r)
# print(r2)

import re
print(dir(re))
