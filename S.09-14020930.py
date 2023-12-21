# Library os dar emtehan nemyad
#import os
# print(os.getcwd()) # cwd: current working directory - mahl zakhire code feeli
#os.mkdir() # make directory - tozih mofasari dare ke sare class be hamin had ektefa shod
#os.walk # Ostad taghriban chizi dar bare walk nagoft, vali be tor pishrafte tar address code ro dakhel file mide
# os.listdir() # list directory - kol file haye python save roye dastgah

##########################################################################
# import time
# print(time.time()) #python az zaman epoch
# Return the time in seconds since the epoch as a floating point number.
# Epoch: The epoch is the point where the time starts, the return value of time.gmtime(0). It is January 1, 1970, 00:00:00 (UTC) on all platforms.

#print(time.gmtime(0)) #  - python az zaman epoch - arguman mohem
#time.gmtime([secs]): Convert a time expressed in seconds since the epoch to a struct_time in UTC

#print(time.ctime()) # hamin alan

#print(time.ctime(1703175405.0717082)) # check beshe
# time.ctime([secs]): dakhel argumanesh be sanie adad mizarim va in zamane ro ba zaman epoch jam mikone va be ma neshon mide
#print(time.ctime(time.time())) # shaiad in code betone manzor ro behtar enteghal bede

#time.sleep() # time.sleep([sec]): baraye delay andakhtan
# mesal add kardan delay
# import time
# for i in range(5):
#     print(i)
#     time.sleep(4)

# Library -> Module -> Function

a = [1, 2, 3]
# print(type(a)) # <class 'list'>
# b = [5, 12.5, "salam", True, [123,"sal"]]
# d = list([1, 55, "test"])
# print(list("salam")) # ['s','a','l','a','m']
# e = [] # []
# print(type(e)) # <class 'list'>
# print(len(b)) #5 tedad azaye list
# print(b[0]) # 5
# print(b[0:2]) # [5, 12.5]
# #b[start,stop,step] stop not included itself
# bb = b[4]
# print(bb[1]) # "sal"
# print(bb[-1]) # "sal"

# for i in b: #kol list b ro print mikone
#     print(i)
# 5
# 12.5
# salam
# True
# [123, 'sal']

# a.append(5) # ezafe kardan 5 be tah list
# print(a) # [1, 2, 3, 5]
# a.insert(0,8) # (index, add ) baghie ro hool mide samt rast
# print(a) # [8, 1, 2, 3, 5]

# n = int(input("please enter a number: "))
# for i in range (1,n+1):
#     for j in range (1, i+1):
#         print (i,"\t",end='')
#     print()
