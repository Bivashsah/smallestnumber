#List=List is the collection of multiple data enclosed with in big brackets and each data is separated by comma(,)
#It is mutable(can) in nature but string is immutable and ordered and duplicat in nature.
#Mutable example...............................................
# a=[3,4,5,6]
# a[0]=4
# print(a) #output becomes like [4,4,5,6]
#................................................................
#syntax=[data1,data2......]
#eg. a=[1,2,'bivash',(6,7),[3,4,5]]
#Empty list...a=[]
#............................................................
# a=[1,2,3]
# a[0]=5
# print(a)
#................................................................
#can't do like this  because sring is immutable
# name="bivash"
# name[0]=k
# print(k)
#.......................................................................
#In loop
# a=[1,2,3]
# for i in a:
#     print(i)
#..............................
# a=['suman',[2,3,4]]
# for i in a:
#     for j in i:
#         print(j)
#.................................................
#loop inside loop....................................................
# a=['bivash',(2,3,4,50)]
# for i in a:
#     for j in i:
#         print(j)
#output
# b
# i
# v
# a
# s
# h
# 2
# 3
# 4
# 50
#...................................................................
#index value print............................................
# a=['bivash',[2,3,4],6,7]
# print(a[0])
#output(bivash).....................................................
#Multiple indexing.....................................................
# a=['bivash',['giga',4,5],8,9,11]
# #print(a[0][2])# here is v print
# print(a[1][0][3])#here is a print
#.......................................................................

#slicing in list.........................................
# a=['Bivash',["Binay"],7,8,(5,6)]
# print(a[::-1])
# print(a[0:5:1])
#Method of list...................................................

#1.append("argument")=It add that argument at the last position 
#  a=['suman',1,3.1]
# a.append("bivash")
# print(a) #it print=['suman',1,3.1,"bivash"]
#.............................................................
# print(a.append("ram"))#can't do like this................................

#2.clear()=It clear the list and give empty list...................................
# a=['bivash',['giga',4,5],8,9,11]
# a.clear()
# print(a)#output is =[]
#....................................................................................

#3.del a # del is kind of keyword.................................................
# a=['bivash',['giga',4,5],8,9,11]
# del a
# print(a)# a is not define
#...................................................................................

#4.copy()=copy the values of a into b.................................................................
# a=['bivash',['giga',4,5],8,9,11]
# b=a.copy()
# print(b)
#.................................................

#5.count()=it count how many number are present in list and it take at least one argument and mostely use for list type number........................................
# a=['biash',1,2,3,4,1]
# print(a.count(1))#it count the how numbers 1 is present in this list
#............................

#6.Extend()=It add the list in the last position and it take argument......................................
# a=['biash',1,2,3,4]
# a.extend(['bivash',7,5,6])
# print(a)#output is=['biash',1,2,3,4,'bivash',7,5,6]///////////////////////////
#.......................................

#3.index()=..............................................
# a=['biash',1,2,3,4]
# print(a.index(2))
#...................................

#insert(insert in specific position)
# a=['biash',1,2,3,4]
# a.insert(1,'ram')
# print(a)
#..................................................
#pop(only last value out)...........................
# a=['biash',5,2,3,4]
# a.pop(1)#position 1 value is remove
# print(a)
#...........................................
# a=['biash',1,2,3,4]
# a.reverse()
# print(a)
#.....................................
#sort(mostely use for numeric data )
# a=[2,5,8,1,9,3]
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)
#..................................................
#Remove................................
# a=['bivash',1,2,3,4]
# a.remove('bivash')
# print(a)
#sorted(must be put in another variable while we do not put in sort method)....................................................
# a=['biash',1,2,3,4]
# b=a.sorted()
# print(a)
#..................................................................
#Addition of two list.............................................
# a=['biash',1,2,3,4]
# b=['biash',1,2,3,4]
# new_list=a+b
# print(new_list)
#..........................................................
# y=[5,6]
# n=len(y)
# for i in range(n):
#     print(i,y[i])
#...........................................................
# list=[1,2,3]
# add=0
# for i in list:
#     add+=i
# print(add)
#...............................................................
# r=[11,12,13,50]
# for i in range(1,4):# or (0,3)
#     if r[0]>r[i]:
#         r[0]=r[i]
# print(f'{r[0]} is the smallest number')
#...........................................................



















        




