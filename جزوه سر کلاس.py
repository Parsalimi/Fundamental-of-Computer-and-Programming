#write a code that calculates the equation: 1!+2!+3!+...+n!
n=int(input("enter the no:"))
f=1
sum=0
for k in range(1,n+1):
    f*=k
    sum+=f
    print(sum)
#write a code that gets an int and calculates y and prints it if:
#x2-7x+13 x>0 , #y=5 x=0 , # 2x-6 x<0
x=int(input("enter your number"))
y=1
if x>0:
    y=x*x-7*x+13
elif x==0:
    y==5
else:x<0
y=2*x-6
print(y)
#write a code that prints out a left point pyramid

#1
#1 2
#1 2 3
#1 2 3 4
a=int(input("input the number: "))
for i in range (1,a+1):
    for j in range (1,i+1):
        print (j,"\t",end='')
        #salam be srcs
edited by emaan.
