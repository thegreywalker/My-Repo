#Q1. Write a program in python to convert temperature from Fahrenheit to Celsius.
# user_input = float(input("Enter temperature measure in Fahrenheit scale: "))
# C_measure = (user_input-32)*5/9
# print("The temperature measure in Celsius is", C_measure)



#Q.2. Write a program in python to convert temperature from Celsius to Fahrenheit
# user_temp_input = float(input("Enter temp measure in Celsius scale: "))
# F_measure = ((n*9/5)+32)
# print("The temperature measure in Fahrenheit is", F_measure)


# """ Q.3.Find out roots of a quadratic equation whose polynomials will be given by user """


# from math import *


# a = int(input("Enter the Value of A: "))
# b = int(input("Enter the Value of B: "))
# c = int(input("Enter the Value of C: "))

# d = pow(b,2) - (4*a*c)
# sum1 = (-b + sqrt(d))/(2*a)
# sum2 = (-b - sqrt(d))/(2*a)
# print(f"The Roots of the Equation are {sum1} & {sum2}")



# Q.4. Write a program in python to generate a report card of a students according to CBSE grade system. User will input 6 subject marks (English, Bengali/Hindi, Physics, Chemistry, Biology and Computer).Find out the total mark and grade. The grade will be calculated as follows:
# 91-100 – “A+”
# 81-90 – “A”
# 71-80 – “B+”
# 61-70 – “B”
# 51-60 – “C”
# 41-50 – “D”
# 31-40 – “E”
# Below 40 – “Fail”


"""
input_xm_total = float(input("Enter full marks of exam: "))
input_eng = float(input("Enter english marks: "))
input_2ndLang = float(input("Enter 2nd Lang. marks: "))
input_Phy = float(input("Enter Physics marks: "))
input_Chem = float(input("Enter Chemistry marks: "))
input_Bio = float(input("Enter biology marks: "))
input_CS = float(input("Enter computer science marks: "))

total_marks = (input_eng) + (input_2ndLang) + (input_Phy) + (input_Chem) + (input_Bio) + (input_CS)
print("Your total marks is", total_marks)
grade = (total_marks/(input_xm_total*6))*100
print("Your percentage is",grade,"%")
if grade >=91  and grade <= 100: 
    print("Your grade is A+")
if grade>=81 and grade <=90:
    print("Your grade is A")
if grade >=71 and grade<= 80:
    print("Your grade is B+")
if grade >=61 and grade <=70:
    print("Your grade is B")
if grade >=51 and grade<=60:
    print("Your grade is C")
if grade >=41 and grade<=50:
    print("Your grade is D")
if grade >= 31 and grade <=40:
    print("Your grade is E")
if grade <=40:
    print("You failed this examination")
    print("Better luck next time")
"""
# def Grader(score):
#     if score >= 91:
#         return "A+"
#     if score >= 81 and score <= 90:
#         return "A"
#     if score >= 71 and score <= 80:
#         return "B+"
#     if score >= 61 and score <= 70:
#         return "B"
#     if score >= 51 and score <= 60:
#         return "C"
#     if score >= 41 and score <= 50:
#         return "D"
#     if score >= 31 and score <= 40:
#         return "E"
#     if score <= 30:
#         return "Fail"


""" Alternative """


# marks_container = input("Enter the Marks of 6 Subjects: ")
# list_container = marks_container.split(", ")
# sum = 0

# for val in list_container:
#     num = int(val)
#     sum = sum + num

# percent = (sum/600)*100
# x = Grader(percent)
# print("==========================================================")
# print("=           Satish Chandra Memorial School               =")
# print("=                    REPORT CARD                         =")
# print("==========================================================")
# print("= NAME : Apurba Ghosh                     CLASS : XI     = ")
# print("= ROLL NO. : 5                            SEC :    C     =")
# print("=           --------------------------------             =")
# print("=                                                        =")
# print("=                 SUBJECTWISE MARKS                      =")
# print("=                                                        =")
# print("=                                                        =")
# print(f"=  English:     {list_container[0]}                                       =")
# print(f"=  Bengali:     {list_container[1]}                                       =")
# print(f"=  Physics:     {list_container[2]}                                       =")
# print(f"=  Chemistry:   {list_container[3]}                                       =")
# print(f"=  Biology:     {list_container[4]}                                       =")
# print(f"=  Computer:    {list_container[5]}                                       =")
# print("=                                                        =")
# print("=                                                        =")
# print("=                                                        =")
# print("=                                                        =")
# print("=                                                        =")
# print("=                                                        =")
# print("=                                                        =")
# print(f"= The Total Marks is {sum}                                 =")
# print(f"= The Grade Obtained is {x}                               =")
# print("=                                                        =")
# print("==========================================================")






#Q.5.Write a program in python to print first 100 even numbers
"""
count = 0
for i in range(0,200):
  if i%2 == 0:
      print(i, end = " ")
          if count == 100:
                break
  else:
      continue
  count += 1
"""


#Q.6. Write a program in python to print all the multiples of 5 from 1 to 100 

"""
for i in range(1,101):
  if i%5 == 0:
      print(i, end = " ")
                           
"""

#Q.7. Write a program in python to print the following series : 
# 1! + 2! + 3! + …………………..+N!
"""
sum = 0
fact = 1 
input_num = int(input("Enter number: "))
for i in range(1, input_num+1):
  fact = fact*i
    sum += fact
    print(sum) 
"""


"""
Q.8.Write a program in python to print the following series :

X1+ X2 + X3 + …………………..+Xn
"""


# input1 = int(input("Enter number: "))
# extend = int(input("Enter iterable value: "))
# sum = 0
# for i in range(1, extend+1):
#     sum = sum + pow(input1,i)

# print(sum)

"""
 Q.9.Write a program in python to print the following series :

 1^1+ 5^5 + 10^10 + …………………..+N^N
"""
# range1 = int(input("Enter range: "))
# sum = pow(1,1)
# for i in range(0, range1):
#     func = i*5
    
#     sum = sum + pow(func,func)

# print(sum-1)

"""
Q.10.Write a program in python to print the following series :

1/x^1 + 2/x^2 + 3/x^3 + …………………..+N/x^N
"""

# extend = int(input("Enter iterable value: "))
# sum = 0
# for i in range(1, extend+1):
#     m = i/pow(extend,i)
#     sum = sum + m

# print(sum)



"""
Q.11.Write a program in python to print the following series :

1! + 2! + 3! + …………………..+N!
"""

# user_input = int(input("Enter number: "))

# fact = 1
# for i in range(1,user_input+1):
#     fact *= i
#     sum+=fact
# print(sum)


"""
Q.12. Write a program in python to print factorial of a number given by user.
"""

# user_num = int(input("Enter number: "))
# fact = 1
# for i in range(1, user_num+1):
#     fact*=i
# print(fact)


"""
Q.13. Write a program in python to check whether a user given number is an Armstrong number or not.
"""
# num_input = int(input("Enter number: "))
# m = num_input
# sum = 0
# temp = num_input
# count = 0
# while num_input!=0:
#     num_input//=10
#     count = count+1
# for i in range(0, count):
#     num =temp%10
#     sum = sum + pow(num,count)
#     temp//=10
# if sum != m:
#     print("The entered number is not an Armstrong Number.")
# else:
#     print("The entered number is an Armstrong Number.")


"""
Q.14. Write a program in python to print Fibonacci series upto N terms given by user
"""
"""Unpacking the list where all the elements in the list are <class int>"""

# num_input = 6
# first_term = 0
# scnd_term = 1
# list1 =[0, 1]
# for i in range(0,num_input-2):
#     thrd = scnd_term+ first_term
#     first_term = scnd_term
#     scnd_term = thrd
#     list1.append(thrd)
# print(f"The fibonacci Series upto {num_input}th is:", end =" ")
# print(*list1, sep = ", ")


"""Using .join() where all the elements in the list are <class str>"""
# num_input = 6
# first_term = 0
# scnd_term = 1
# list1 =['0', '1']
# for i in range(0,num_input-2):
#     thrd = scnd_term+ first_term
#     first_term = scnd_term
#     scnd_term = thrd
#     list1.append(str(thrd))
# print(f"The fibonacci Series upto {num_input}th is:", end =" ")
# print(*list1, sep = ", ")
# #print(", ".join(list1))

'''
Q.15. Write a program in python to find out GCD of two numbers given by user.
'''

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = 0
if num1>num2:
    while num2 != 0:
        num3 = num1%num2
        num1 = num2
        num2 = num3
    print(num1)
if num2>num1:
    while num1 != 0:
        num3 = num2%num1
        num2 = num1
        num1 = num3
    print(num2)



































