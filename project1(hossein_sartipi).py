#doostan aziz age naneveshtid run konid faghat, code az khat chehel start mikhore






































#region information

from os import system
from random import randint
import random
correct_answers = 0
wrong_answers = 0
temp = True

system("cls")

sin0 = "sin(0)"
sin30 = "sin(pi/6)" 
sin45 = "sin(pi/4)"
sin60 = "sin(pi/3)"
sin90 = "sin(pi/2)"

cos0 = "cos(0)"
cos30 = "cos(pi/6)"
cos45 = "cos(pi/4)"
cos60 = "cos(pi/3)"
cos90 = "cos(pi/2)"

tan0 = "tan(0)" 
tan30 = "tan(pi/6)"
tan45 = "tan(pi/4)"
tan60 = "tan(pi/3)"
tan90 = "tan(pi/2)"

data1 = [sin0, sin30, sin45, sin60, sin90, cos0, cos30 , cos45, cos60, cos90, tan0, tan30, tan45, tan60, tan90]
data2 = ["0", "1/2", "radical2/2", "radical3/2", "1",
        "1", "radical3/2", "radical2/2", "1/2", "0",
        "0", "radical3/3", "1", "radical3", "undefined",]
data3 = []

#endregion

#region chart
print("Hello, answer questions according to the chart", "\n")

print("-----------------------------------------------------------------------------------------------------------")
print("|   sin0=0   |   sin30=1/2          |   sin45=radical2/2    |   sin60=radical3/2   |   sin90=1            |")
print("|   cos0=0   |   cos30=radical3/2   |   cos45=radical2/2    |   cos60=1/2          |   cos90=0            |")
print("|   tan0=0   |   tan30=radical3/3   |   tan45=1             |   tan60=radical3     |   tan90=undefiened   |")
print("-----------------------------------------------------------------------------------------------------------")

    
input("If you are ready to start press ENTER : ")
system("cls")

#endregion

#region game
while len(data3)<15:
    x = (random.choice(data1))
    if x not in data3:
        data3.append(x)

        flag = True
        lent = 0
        while flag:

            print("____________________")
            print(x, ": ", end="")
            y = (input())
            system("cls")
            wrong_answers += 1
            print("Wrong(Bebakhshina)")
            print("____________________")
            print("correct_answers : ", correct_answers)
            print("wrong answers :", wrong_answers)


            if data1[0+lent] and y==data2[0+lent]:
                    flag = False
            if data1[1+lent] and y==data2[1+lent]:
                    flag = False
            if data1[2+lent] and y==data2[2+lent]:
                    flag = False
            if data1[3+lent] and y==data2[3+lent]:
                    flag = False
            if data1[4+lent] and y==data2[4+lent]:
                    flag = False 
            if data1[5+lent] and y==data2[5+lent]:
                    flag = False
            if data1[6+lent] and y==data2[6+lent]:
                    flag = False
            if data1[7+lent] and y==data2[7+lent]:
                    flag = False
            if data1[8+lent] and y==data2[8+lent]:
                    flag = False
            if data1[9+lent] and y==data2[9+lent]:
                    flag = False
            if data1[10+lent] and y==data2[10+lent]:
                    flag = False 
            if data1[11+lent] and y==data2[11+lent]:
                    flag = False 
            if data1[12+lent] and y==data2[12+lent]:
                    flag = False 
            if data1[13+lent] and y==data2[13+lent]:
                    flag = False 
            if data1[14+lent] and y==data2[14+lent]:
                    flag = False
            
                   
                
                   
        system("cls")

        correct_answers += 1
        wrong_answers -= 1
        print("Right(Doorood bar to)")
        print("correct_answers : ", correct_answers)
        print("wrong answers :", wrong_answers)

#endregion

#region ending
        
print("Bache ha dast bezanin zase kasi ke tamom kard, bebinin cheghadr bahooshe va nist hichjore ablah")

#endregion            