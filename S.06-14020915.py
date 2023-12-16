################## Lecture ##################
#----------------001----------------#
#for i in "salam":
#    print(i,"\t", end = ' ')

#----------------002----------------#
#for i in "salam":
#    print("salam")

#----------------003----------------#
#for i in "100":
#    print("salam")

#----------------004----------------#
#for i in range (1,10,1):
#    print(i)

#----------------005----------------#
#for i in range (0,1000,10):
#    print(i)

#----------------006----------------#
#for i in range (1, 1+3):
#    for j in range (10, 600+1, 100):
#        print(i,":",j)

#----------------007----------------#
#for i in range (1, 10+1):
#    for j in range (1, 10+1):
#        print(i*j,"\t",end=' ')
#    print()

#----------------008----------------#
#for i in range (0, 101,10):
#    print(i)
#    if i == 20:
#        continue
#    print(i*2)

#----------------009----------------#
#a=0
#while a<100:
#    print(a)
#    a+=1

#----------------010----------------#
#a = 1245
#counter = 0
#while a!=0:
#    a = a//10
#    counter += 1
#    print(counter)

#----------------011----------------#
#import math
#s = int(input("Lotfan adad mored nazar ra vared konid: "))
#h = math.floor(s / 3600)
#s = s - h*3600
#m = math.floor(s / 60)
#s = s - m*60
#print(h,":",m,":",s)

#----------------012----------------#
#a = int(input("enter a: "))
#b = int(input("enter b: "))
#c = int(input("enter c: "))
#if (a==b) or (a==c) or (a==b):
#    print("Yes")
#else:
#    print("No")

#----------------013----------------#
#a = int(input("give me the num: "))
#for i in range (1,a + 1,2):
#    print(i)

#----------------001----------------#
#a = int(input("give me the num: "))
#x = 0
#for i in range (1,a + 1, 2):
#    x = i + x
#    print(i,"\t","Sum: ",x)
#print("Total Sum: ", x)

#----------------014----------------#
#n = int(input("Tedad daneshjoyan ra vared konid: "))
#sum = 0
#for i in range (1,n+1):
#    a = int(input("Nomre daneshjo ",i,"th ra vared konid"))
#    sum = a + sum

#print(sum/n)

#----------------015----------------#
# n = int(input("Tedad n ra vared konid: "))
# sumO = 0
# sumE = 0
# for i in range(1,n+1,2):
#     print("1/",i," ", end="")
#     sumO = 1/i + sumO
# print
# for j in range(-2,-n-1,-2):
#     sumE = 1/j + sumE
#     print("1/",j," ", end="")
# print(sumE+sumO)

#----------------016----------------#
#n = int(input("n ra vared konid: "))
#f = 1
#for i in range(n,1,-1):
#    f = i * f

#print(f)

################## Assignment ##################
# for i in range (1, 10+1):
#    for j in range (1, 10+1):
#        print(i*j,"\t",end='')
#    print()

# n = int(input("Tedad n ra vared konid: "))
# sumO = 0
# sumE = 0
# for i in range(1,n+1,2):
#     print("1/",i," ", end="")
#     sumO = 1/i + sumO
# for j in range(-2,-n-1,-2):
#     sumE = 1/j + sumE
#     print("1/",j," ", end="")
# print(sumE+sumO)

n = int(input("n ra vared konid: "))
f = 1
for i in range(n,1,-1):
   f *= i
print(f)