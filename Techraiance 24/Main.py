# import math

# import random

import os 

# x = 273

# print(type(x))

# var1 = 2+2j

# print(type(var1))

# var2 = True 

# print(type(var2))

# var3  = "kelvin"

# print(type(var3))

# # A collection of dissimilar datatypes which is ordered and can be changed is known as list data structure 

list1 = [6+8j,273,True,"bool",5678.98765]
# print(list1)
# list1.insert(3,"abc")
# print(list1)

# tuple1 = ("king",1,"power",True)

# print(len(tuple1))

# # sets are datatypes which are unordered immutable unindexxed
# set1 = {"abc",1234,789.983,True}
# print(set1)
# set2 = {"kelvin",273,9838.49}
# print(set1.union(set2))

# dict1 = {"Brand":"Ferrari",
#          "model":"laferrari",
#          "year":"2020",
#          "year":"2017",
#          "name":"laferrari 20th aniversary model"}
# print(dict1)
# print(dict1["Brand"])
# print(dict1["name"])
# print(dict1["year"])
# print(dict1["model"])


# #OPERATORS

# x2 = 23
# y = 35
# print(x2+y)
# print(x2*y)
# print(x2//y)
# print(x2/y)
# print(x2-y)
# print(x2%y)

# print(x2>=y)

# #CONDITIONS

# z = int(input("Num1: "))
# a = int(input("Num2: "))
# b = int(input("Num3: "))
# if a>z and b>z:
#     print("a and b is greater than z")
# elif a>z or b>z :
#     print("a or b is greater than z")
# elif not a>b:
#     print("a is not gerater than b")



# #Functions

# def gg(a):
#     if a%2 == 0:
#         print("even")
#     else:
#         print("odd")
        
# gg(a)

# for i in range(4,39,2):
#     print(i)
#     if i == 30:
#         break
#     else:
#         continue
    
#MODULES

# python modules are basically files containing builtin functions , classes, variables.
# there ar emany python modules each with specific work alloted.
# there are 2 types of modules built-in and other is user defined.

# import math      

# print(math.sqrt(144))
# g = int(input("Number: "))
# result = math.factorial(g)
# print(f"the factorial of {g} is {result}")
# radian = int(input("Radian: "))
# sin = math.sin(radian)
# print(sin)
# print(math.pi)
# print(math.e)

# cwd = os.getcwd()
# print(f"Current Working Directory {cwd}")
# os.mkdir("random")
# print(os.listdir())
# os.rmdir("random")
