################## Lecture ##################
# # Library datetime
# import datetime
# print(datetime.date.today())
#
# # datetime Module / date Sub-Module
# from datetime import date
# print(date.today())

################## Assignment ##################
# Barnameyi benevisid ke ebarat ro be ro ra namayesh dahad
# 7 6 5 4 3 2 1
# 6 5 4 3 2 1
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
# n = int(input("Please enter your number: "))
# for i in range(n, 0, -1):
#     for j in range(i, 0, -1):
#         print(j,"\t",end="")
#     print()

# Barnameyi benevisid ke adad sahih va mosbat n ra az vorodi daryaft konad va bozorgtarin ragham aan ra namayesh dahad
n = int(input("Please enter your number: "))
nStr = str(n)
max = 1
for i in range(len(str(n))):
    if int(nStr[i:i+1]) > max:
        max = int(nStr[i:i+1])
print("max is: ", max)