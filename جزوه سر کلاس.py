#برنامه ای بنویسید که عدد صحیح و مثبت n را از ورودی دریافت کند وعبارت (...+!3+!2+!1)
n=int(input("enter the no:"))
f=1
sum=0
for k in range(1,n+1):
    f*=k
    sum+=f
    print(sum)
#   برنامه ای بنوسید که عدد صحیح مثبت n را از ورودی دریافت کند و مجموع ارقام آن عدد را به صورت خروجی نمایش بده

 #برنامه ای بنوسید کهx را از ورودی دریافت کند و y را محاسبه و چاپ نماید
#x2-7x+13 x>0
#y=5 x=0
# 2x-6 x<0
x=int(input("enter your number"))
y=1
if x>0:
    y=x*x-7*x+13
elif x==0:
    y==5
else:x<0
y=2*x-6
print(y)
#برنامه ای بنویسید که عبارت زیر را نمایش دهد

#1
#1 2
#1 2 3
#1 2 3 4
a=int(input("input the number: "))
for i in range (a):
    for j in range (i):
        print (j,"\t",end='')
        #salam be srcs
edited by emaan.
