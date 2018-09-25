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

# import re
# print(dir(re))

# import json
# 
# json_str = '[{"name":"zhao", "age":50, "flag":false}, {"name":"zhao", "age":50}]'
# 
# student = json.loads(json_str)
# 
# print(type(student))
# print(student)

# from enum import Enum
# 
# yellow = 1
# green = 2
# 
# a = {
#         'yellow':1, 
#         'green':2
#         }
# # 可以改变内容
# 
# class TypeDiamond():
#     yellow = 1
#     green = 2
# # 可变
# # 没有防止相同标签的功能

# from enum import Enum
# 
# class VIP(Enum):
#     YELLOW = 1
#     GREEN = 1
#     BLACK = 3
#     RED = 4
# # 内容不能轻易更改
# # 可以遍历
# 
# for i in VIP:
# # for i in VIP.__members__:
#      print(i)
#  
# print(VIP(3))
# 
# # 获取标签的值
# # print(VIP.GREEN.value)
# # print(VIP.GREEN.name)
# # print(VIP['GREEN'])
# 
# from enum import IntEnum

from datetime import datetime
def f(n):
    for i in range(9):
        begintime = datetime.now()
        for j in range(n):
            pass
        endtime = datetime.now()
        time = endtime - begintime
        print("{0:2d}: n = {1}, time = {2:.6f} milliseconds".format(i+1, n, time.total_seconds()*1000))

import sys
if len(sys.argv) > 1:
    n = int(sys.argv[1])
else:
    n = 100000
f(n)
