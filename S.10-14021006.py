# a = [1,2,3]
# a.remove(1) #argoman haman adadi ke mikhaim paak beshe
# print(a)
# list.pop() #argoman index midim va dar ein haal adad hazf shode ro neshon mide
# list.clear() # kol list ro paak mikone

################################
# adad zoj va fard ra namayesh dahad
# a = [1,2,3,4,5,6,7,8,9,11]
# even = []
# odd = []
# for i in a:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(f"Even Numbers: {even}")
# print(f"Odd Numbers: {odd}")

################################
# adad aval ra namayesh bede


################################
# def func1():
#     print("Hello world")
# func1()

################################
# def func2(n):
#     print("my name is: ", n)
#
# func2("mmd")
# func2("hossein")
################################
#
# def func3(firstName, lastName):
#     print("My name is", firstName + " " + lastName)
# func3("Parsa", "Salimi")

################################
# def func4(x,y):
#     return x + y
#
# print(func4(3,5))
################################

# n = int(input("Enter a number: "))
# def timeFive(x):
#     return x*5
# print(timeFive(n))

################################
# def func(*n):
#     print("the youngest child is: ", n[2])
# func("ali", "sepeher", "Melika", "keyvan")

################################
# barnamei benevisid ke meghdar ebarat zir ra dar khoroji namayehs dahad ba estefade az function
# P(n,r) = n!/(n-r)!
# in code eshtebah ast
# def factoriel(x):
#     f = 1
#     for i in (1, x+1):
#         f *= i
#     return f
#
#
# n = int(input("n?: "))
# r = int(input("r?: "))
# print(factoriel(n) / factoriel(n-r))
################################

# def fibonachi (n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return (n-1) + (n-2)
# x = int(input("enter: "))
# print(fibonachi(x))