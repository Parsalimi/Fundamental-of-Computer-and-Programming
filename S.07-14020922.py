################## Lecture ##################
# n = int(input("Enter the no: "))
# f = 1
# sum = 0
# for k in range(1, n+1):
#     f *= k
#     sum += k
# print(sum)
#######################################
# Barnamei benevisid ke adad sahih va mosbat n ra az vorodi daryaft konad va majmoeh argham aan adad ra be sorat khoroji namayesh bede
# n = int(input("Please enter a number: "))
# s = 0
# while n > 0:
#     s += n % 10
#     n //= 10
# print(s)
#######################################
# Barnamei Benevisid x ra az khoroji daryaft konad va y ra mohasebe kone va print kone
# x > 0     y = x^2-7x+13
# x = 0     y = 5
# x < 0     y = 3x-6
# x = int(input("Enter the no: "))
# if x == 0:
#     y = 5
# elif x > 0:
#     y = x*x-7*x+13
# else:
#     y = 3*x+6
# print(y)

#######################################
#write a code that prints out a left point pyramid
#1
#1 2
#1 2 3
#1 2 3 4
# a=int(input("input the number: "))
# for i in range (1,a+1):
#     for j in range (1,i+1):
#         print (j,"\t",end='')
#         #salam be srcs
# #edited by emaan.


################## Assignment ##################

# Barnamei benevisid ke hasel ebarat ro be ro ra mohasebe konad
# P(n,r) = n! / (n-r)!
# n = int(input("n ra vared konid: "))
# r = int(input("r ra vared konid: "))
#
# def factorial(number):
#     Factorial = 1
#     for i in range(1, number+1):
#         Factorial *= i
#     return Factorial
#
# print(f"P(n,r) = {factorial(n) / factorial(n-r)}")

# Barnamei benevisid ke hasel ebarat zir ra chap konad
# 1 + x^1/1! + x^2/2! + ... + x^n/n!

# import os
# while True:
#     os.system('cls')
#     n = int(input("n ra vared konid: "))
#     x = int(input("x ra vared konid: "))
#     if n >= 0:
#         break
#
# def factorial(number):
#     if number == 0:
#         return 1
#     else:
#         Factorial = 1
#         for i in range(1, number+1):
#             Factorial *= i
#         return Factorial
#
# sum = 0
# for i in range(0, n+1):
#     sum += (x**i/factorial(i))
# print(sum)

#Barnamei benevisid ke hasel ebarat ro be ro ra hesab konad
#1
#1 2
#1 2 3
#1 2 3 4
# n = int(input("input the number: "))
# for i in range (1, n+1):
#     for j in range (1,i+1):
#         print (j,"\t",end='')
#     print()

# Barnamei Benevisid x ra az khoroji daryaft konad va y ra mohasebe kone va print kone
# x > 0     y = x^2-7x+13
# x = 0     y = 5
# x < 0     y = 3x-6
# x = int(input("Enter the no: "))
# if x == 0:
#     y = 5
# elif x > 0:
#     y = x*x-7*x+13
# else:
#     y = 3*x+6
# print(y)

# Namayesh Majmoeh Argham
# n = int(input("Please enter a number: "))
# l = 0
# while n > 0:
#     l += n % 10
#     n //= 10
# print(l)