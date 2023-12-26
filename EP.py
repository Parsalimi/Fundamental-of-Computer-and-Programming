# Exam Preparation
# Vorodi ra daryaqft konad va baraks be ma neshan dahad
# x = int(input("Please enter a number: "))
# i = 0
#
# while x != 0:
#     r = x % 10
#     x = x // 10
#     i = i * 10 + r
#
# print(i)
################################################################
# Factoriel
# n = int(input("please enter your n: "))
# f = 1
# for i in range(1, n+1):
#     f *= i
#
# print(f)
################################################################
# 1 + 1/2 + 1/4 + 1/8 + ... + 1/2n
# n = int(input("please enter your n: "))
# sum = 1
# if n == 1:
#     print(f"answer: {sum}")
# elif n > 1:
#     for i in range(1, n+1):
#         sum += 1/(2*i)
#     print(f"answer: {sum}")
################################################################
# shekl zir ra chap konad
# *
# **
# ***
# ****

# n = int(input("please enter your n: "))
# for i in range(1, n+1):
#     print("*"*i,end='')
#     print()
################################################################
# adad chand raghami ast?
# import math
# n = int(input("please enter your n: "))
# counter = 0
# while n != 0:
#     n = math.floor(n/10)
#     counter += 1
# print(counter)
################################################################
# chand adad az vorodi begirad va tedad adad zooj ra begoiad
# n = int(input("how many numbers would you like to test: "))
# i = 1
# evenCounter = 0
# while i <= n:
#     x = int(input(f"Please enter your {i}th number: "))
#     if x % 2 == 0:
#         evenCounter += 1
#     i += 1
# print(f"There was {evenCounter} even number there")
################################################################
# chand adad az vorodi begirad va average ra neshan dahad
# n = int(input("how many numbers would you like to test: "))
# i = 1
# sum = 0
# while i <= n:
#     x = int(input(f"Please enter your {i}th number: "))
#     sum += x
#     i += 1
# print(f"The avg is: {sum/n}")
################################################################
# chand adad az vorodi begirad va max va min ra moshakhas konad
# n = int(input("how many numbers would you like to test: "))
# i = 1
# max = 0
# min = 0
# while i <= n:
#     x = int(input(f"Please enter your {i}th number: "))
#     if i == 1:
#         max = x
#         min = x
#     if x > max:
#         max = x
#     elif x < min:
#         min = x
#     i += 1
# print(f"Max: {max}, and Min: {min}")
################################################################
# 2 adad ja be ja beshe ba 2 moteghayer
# a=int(input("num:"))
# b=int(input("num:"))
# a=a+b
# b=a-b
# a=a-b
# print(f"{a} , {b}")
################################################################
# yek adad ra az vorodi begirad va zoj ya fard bodanash ra namayesh dahad
# n = int(input("no: "))
# if n % 2 == 0:
#     print("It is Even")
# else:
#     print("It is Odd")
################################################################
# Nomre daneshjo ra begirad va bar asas meyar zir chaap konad
# A - [20,18]
# B - (18,16]
# C - (16,14]
# D - (14,10]
# E - (10,0]
# n = float(input("no: "))
# if n > 18:
#     print("A")
# elif n > 16:
#     print("B")
# elif n > 14:
#     print("C")
# elif n > 10:
#     print("D")
# elif n > 0:
#     print("E")

################################################################
# Karmandi 9% hoghogh maleyat va 10% hoghogh bime mide, hoghogh ra begirid va maleyat va bime ke mide ro hesab konid va hoghogh khales ra namayesh dahid
# income = float(input("Please enter your income: "))
# print(f"Tax: {income*0.09}, Insurance: {income*0.1}, True Income: {income-(income*0.09+income*0.1)}")
################################################################
# Jadval Zarb 10 dar 10
# for i in range(1,10+1):
#     for j in range(1,10+1):
#         print(i*j,end="\t")
#     print()
################################################################
# 1 - 1/2 + 1/3 - 1/4 + 1/5 + ... + 1/n
# n = int(input("n: "))
# oddSum = 0
# evenSum = 0
#
# # Sum odd Numbers
# for i in range(1, n+1,2):
#     oddSum += 1/i
# # Sum Even Numbers
# for i in range(-2,-n-1,-2):
#     evenSum = 1/i
# print(oddSum + evenSum)
################################################################
# Barnamei benevisid ke hasel ebarat ro be ro ra mohasebe konad
# P(n,r) = n! / (n-r)!
# n = int(input("n?: "))
# nFactoriel = 1
# r = int(input("r?: "))
# nrFactoriel = 1
#
# for i in range(1, n+1):
#     nFactoriel *= i
#
# for i in range(1, n-r+1):
#     nrFactoriel *= i
#
# print(f"P({n},{r}) = {n}! / ({n - r})! = {nFactoriel/nrFactoriel}")

################################################################
# Barnamei benevisid ke hasel ebarat zir ra chap konad
# 1 + x^1/1! + x^2/2! + ... + x^n/n!
# n = int(input("n?: "))
# x = int(input("x?: "))
# sum = 0
# f = 1
# for i in range(n):
#     for j in range(1, i+1):
#         f *= j
#     sum += (x**i)/f
# print(sum)

################################################################
#Barnamei benevisid ke hasel ebarat ro be ro ra hesab konad
#1
#1 2
#1 2 3
#1 2 3 4

# n = int(input("n?: "))
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()

################################################################
# Barnamei Benevisid x ra az khoroji daryaft konad va y ra mohasebe kone va print kone
# x > 0     y = x^2-7x+13
# x = 0     y = 5
# x < 0     y = 3x-6
# x = float(input("x?: "))
# if x > 0:
#     print(x**2 - 7*x + 13)
# elif x == 0:
#     print(5)
# else:
#     print(3*x-6)

################################################################
# Namayesh Majmoeh Argham
# n = int(input("n?: "))
# counter = 0
# while n != 0:
#     n = n // 10
#     counter += 1
# print(counter)


################################################################
# Barnameyi benevisid ke ebarat ro be ro ra namayesh dahad
# 7 6 5 4 3 2 1
# 6 5 4 3 2 1
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
# n = int(input("n?: "))
# for i in range(n, 0, -1):
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     print()

################################################################
# Barnameyi benevisid ke adad sahih va mosbat n ra az vorodi daryaft konad va bozorgtarin ragham aan ra namayesh dahad
# n = int(input("n?: "))
# a = 0
# max = 1
# while n != 0:
#     a = n % 10
#     if a > max:
#         max = a
#     n = n // 10
# print(max)


################################################################
#1
#2 	2
#3 	3 	3
#4 	4 	4 	4
#5 	5 	5 	5 	5
# n = int(input("n?: "))
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(i, end=" ")
#     print()

################################################################
# jam factoriel
# n = int(input("n?: "))
# f = 1
# sum = 0
# for i in range(1, n+1):
#     f *= i
#     sum += f
#
# print(sum)


################################################################
# Barnamei benevisid ke adad sahih va mosbat n ra az vorodi daryaft konad va majmoeh argham aan adad ra be sorat khoroji namayesh bede
# n = int(input("n?: "))
# sum = 0
# while n != 0:
#     sum += n % 10
#     n = n // 10
# print(sum)

################################################################
