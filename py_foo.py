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

# from datetime import datetime
# def f(n):
#     for i in range(9):
#         begintime = datetime.now()
#         for j in range(n):
#             pass
#         endtime = datetime.now()
#         time = endtime - begintime
#         print("{0:2d}: n = {1}, time = {2:.6f} milliseconds".format(i+1, n, time.total_seconds()*1000))
# 
# import sys
# if len(sys.argv) > 1:
#     n = int(sys.argv[1])
# else:
#     n = 100000
# f(n)

#list_x = [1, 0, 1, 0, 0, 1]
#ff = filter(lambda x: True if x ==1 else False, list_x)
#mm = map(lambda x: True if x == 1 else False, list_x)
#print(list(ff))
#print(list(mm))
#fff = filter(list_x)
#print(fff)
#[1, 1, 1]
#[True, False, True, False, False, True]

# while True:
#     try:
#         a = int(input("first number:"))
#         b = int(input("second number:"))
#         d = a/b
#         print(d)
#         break
#     except(TypeError, ValueError, ZeroDivisionError):
#         print("invalid input")
#     finally:
#         print("run")

# with open("foo.py") as f:
#     for line in f:
#         print(line)

# 1
# def bmi(weight, height):
#     bmi = weight/height**2
#     return bmi
# 
# height, weight = eval(input("enter height and weight: "))
# bmi = bmi(weight, height)
# if bmi >= 28:
#     print("too fat: ", bmi)
# elif bmi >= 24:
#     print("fat: ", bmi)
# elif bmi >= 18.5:
#     print("normal: ", bmi)
# else:
#     print("thin: ", bmi)

# 6
# - 3 4 5 
# def proc(n):
#     if n<0:
#         print('-', end = ' ')
#         n = -n
#     if n//10:
#         proc(n//10)
#     print(n%10, end = ' ')
 
# proc(-345)

# 2
# def conv(f):
#     c = 5/9*(f-32)
#     return c
# 
# for f in range(0,301,20):
#    c = conv(f)
#    print("F: {0:3d}, C: {1:5.1f}".format(f, c))

# 3
# n = eval(input("enter a number: "))
# while n != 1:
#     if n % 2 == 0:
#         print(n, "/2 =", end = ' ')
#         n /= 2
#         print(n)
#     else:
#         print(n, "* 3 + 1 =", end = ' ')
#         n = n*3+1
#         print(n)

# 4

# 5
# x = [1, 2, 3, 4]
# i = 0
# for a in x:
#     for b in x:
#         for c in x:
#             if a != b and b != c and a != c:
#                 i += 1
#                 print(i, "{}{}{}".format(a, b, c))
# 

# 6
# for n in range(100, 1000):
#     if n % 37 == 0:
#         m = n%10*100 + n//100*10 + n//10%10
#         if m % 37 != 0:
#             print("false")
#             break
# else:
#     print("true")
# 

# 7
# from math import sqrt
# def f(n):
#     m = int(sqrt(n))
#     l = [1]
#     for i in range(2,m+1):
#         if n % i == 0:
#             if i == n/i:
#                 l += [i]
#             else:
#                 l += [i, n/i]
#     l.sort()
#     if sum(l) == n:
#         return l 
# 
# for i in range(1,1001):
#     l = f(i)
#     if l:
#         print(i,'= 1',end=' ')
#         for j in l:
#             print('+', j, end=' ')
#         print()
# 

# 8

##
# from math import sqrt, floor
# 
# def fac(n):
#     fac_list = [1]
#     for i in range(2, floor(sqrt(n)+1)):
#         if n % i == 0:
#             if i != n//i:
#                 fac_list += [i, n//i]
#             else:
#                 fac_list += [i]
#     return sum(fac_list)
# 
# n = int(input())
# for i in range(1, n):
#     if i == fac(fac(i)) and i < fac(i):
#         print("{}-{}".format(i, fac(i)))
# 

# from math import sqrt, floor
# def prime(num):
#     if num <= 1:
#         return False
#     m = sqrt(num)
#     for i in range(2, floor(m) + 1):
#         if num % i == 0:
#             return False
#     else:
#         return True
# 
# def monisen(no):
#     i = 2
#     while no > 0:
#         if prime(i) and prime(2**i - 1):
#             no -= 1
#         i += 1
#     else:
#         return (2**(i-1) -1)
# 
# print(monisen(int(input())))
# 
# n = int(input("enter a number: "))
# m = n
# s = 0
# while n != 0:
#     s = s *10 + n % 10
#     n //= 10
# 
# 
# 0.
# n = 1234
# s = 0
# 
# 1. 
# s = 4
# n = 123
# 
# 2.
# s = 40 + 3
#     =43
# n = 12
# 
# 3.
# s = 430 + 2
#     =432
# n = 1
# 
# 4.
# s = 4321
# n = 0

hahaha# n = int(input("enter a number: "))hahaha
hahaha# print(n, '=', end=' ')hahaha
hahaha# i = 2hahaha
# while n != 1:
#     while n % i == 0:
#         n //= i
#         if n == 1:
#             print("{}".format(i))
#         else:
#             print("{} *".format(i), end=' ')
#     i += 1
