 #elif inside loop.....................................
# for i in range(1,10):
#     for j in range(i,10):
#         if(i%2==0):
#             break
#     else:
#         print(i)

#while loop........................................
# num=2
# while True:
#     if(num==2):
#         print(num)
#         break
#     else:
#         print("Infinite loop")
#..............................................................
# count=0
# while count!=3:  
#     print('Hello')
#     count+=1
#....................................................................
#Example of calcualtor using while loop...................................
# num1=int(input("Enter the first number"))
# num2=int(input("Enter the second number"))
# while True:
#     print("1.Addition\n,2.Subtraction\n,3.Multiplication\n,4.Division\n")
#     choice=int(input("Enter the choice"))
#     if choice==1:
#         sum=num1+num2
#         print("The sum of two number is=",sum)
#     elif choice==2:
#         sub=num1-num2
#         print("The sunbtraction of two number is=",sub)
#     elif choice==3:
#         mul=num1*num2
#         print("Multiplication of two number is=",mul)
#     elif choice==4:
#         div=num1/num2
#         print("Division of two number is =",div)

#     else:
#         print("You enter wroung choice")
#........................................................................................

#problem in this code once run and you see the problem
# for i in range(1,11):
#     for j in range(i,11):
#         if(i%2==0):
#             print(i)

#.................................................................................
#Even number and odd number
# r=int(input("Enter the any number"))
# while True:
#     if(r%2==0):
#         print("Entered Number is Even number",r)
#         break
#     else:
#         print("Entered numbre is oddd number")
#         break
#..........................................................................................
#Infinite loop example.................................................................
# num=2
# while True:
#  if(num==2):
#   print(num)
#   break
 #.................................................................................... 
 
#string formatting=> Ther are three type of string formatting which are
#1.%
a="Bivash"
b=4
print("my name is %s and my roll number is %i"%(a,b)) #%i is used for integer



