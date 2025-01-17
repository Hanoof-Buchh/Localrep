# WAP to calculate the tax on a given salary, where the tax rate is 10% if the salary is less than 50,000, and 20% if the salary is 50,000 or more.
# sal = float(input("salary: "))
# tax = sal*(0.1 if sal < 50000 else 0.2)
# print("tax: ", tax)

# WAP to input 2 numbers and print  their sum
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# sum = a+b
# print("sum: ",sum)

# WAP to input side of a square & print its area
# side = float(input("enter the side of a square : "))
# print("area: ",side**2)

#  WAP to input two floating point numbers & print their average
# First_num = float(input("Enter the first number: "))
# Second_num = float(input("Enter the second number: "))
# Average = (First_num + Second_num)/2
# print("Average is: ",Average)

# WAP to input 2 int numbers, a and b. Print true if a is greater than or equal to b. If not print false.
# a = int(input("First number: "))
# b = int(input("Second number: "))
# print(a>=b)

#LECTURE2
#str1 = "This is a string"
#str2 = 'hanoof'
#str3 = """This is also a string"""
#print(str2[0:3])

# str = "Hello I am learning python"
# print(str.endswith("hon"))
# print(str.endswith("py"))

# str = "hello my name is hanoof"
# str = str.capitalize()
# print(str)

#str = "Hello i am learning python"
# print(str.replace("o","a"))
#print(str.replace("python","github"))

# str = "hello i am learning python"
# print(str.find("o"))

# str = "hello my name is hanoof. hello i am studying python. hello i am a software developer"
# print(str.count("hello"))
# print(str.count("my"))
# print(str.count("am"))

# WAP to input users first name and print its length
# name = "Hanoof"
# length = len(name)
# print("the length of the string is: ", length)

# WAP to find the occurence of '$' in a string
# str = " iushdfiuh$$uhguygv$$gtyvgvh$4gbvu$ghvhgE$gvhg$vuG$"
# print(str.count("$"))

# marks = int(input("Enter your marks: "))
# if marks>=90 and marks<=100:
#     print("Grade = A")
# elif marks<90 and marks>=80:
#     print("Grade = B")
# elif marks<80 and marks>=70:
#     print("grade = C")
# elif marks<70 and marks>=0:
#     print("Grade = D")
# else:
#     print("invalid marks")

# nested if program
# age = int(input("Enter your age: "))
# if age>=18:
#     if age>=80:
#         print("cannot drive")
#     else:
#          print("can drive")
# else:
#     print("cannot drive")

# WAP to check if a number entered by the user is  even or odd
# num = int(input("Enter the number: "))
# if num%2 == 0 :
#     print("Entered number is even")
# elif num%2 != 0:
#     print("Entered number is odd")
# else:
#     print("Wrong input")

#WAP to find the greatest of 3 numbers entered by the user
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# if a >=b and a>=c:
#     print("Greatest number is: ",a)
# elif b>=a and b>=c:
#     print("Greatest number is: ",b)
# elif c>=a and c>=b:
#     print("Greatest number is: ",c)
                #OR
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# Greatest = a if (a>=b and a>=c) else b if( b>=a and b>=c) else c
# print("Greatest number is: ",Greatest)

#  WAP to check if a number is a multiple of 7 or not
# num = int(input("Enter number: "))
# if num % 7 == 0:
#     print("Number is a multiple of 7")
# else:
#     print("Number is not a multiple of 7")

#LECTURE3

#student = ["Hanoof",12,98.60,"Aman",13,99.90,"Ashaz",14,76.49]
#print(student[0])
#print(student[0:3])
#student.append("aryan")

#List = [2 , 1 , 3 , 4 ]
# List.append(5)
#List.sort(reverse=True)
#print(List)

# List = [4 , 1 , 3 , 2 , 5]
# List.reverse()
# print(List)

# List = [4 , 1 , 3 , 2 , 5]
# List.insert(1,7)
# print(List)

# List = [4 , 1 , 3 , 2 , 5]
# List.remove(4)
# print(List)

# List = [4 , 1 , 3 , 2 , 5]
# List.pop(2)
# print(List)

# tup = (1,2,3,4,5,6,7,8,9)
# print(tup)

# tup = (2 , 4 , 1 , 5 , 9 , 6 , 3)
# print(tup.index(4))

# tup = (3 , 6 , 1 , 3 , 4 , 7 , 4)
# print(tup.count(4))

# WAP to ask the user to enter three favourite movies and store them in a list
# movies = []
# mov1 = input("enter first movie: ")
# mov2 = input("enter second movie: ")
# mov3 = input("enter third movie: ")
# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)

#WAP to check if a list contains a palindrome of elements. (Hint:- use copy() method)
#list1 = [1 , 3 , 4 , 5 , 4 , 3 , 1]
#copy_list1 = list1.copy()
#copy_list1.reverse()
#if list1 == copy_list1:
#    print("palindrome")
#else:
#    print("not palindrome")
# WAP tp count the number of students with the "A" grade in the following tuple
# tup = ("A" , "B" , "C" , "A" , "A" , "B" , "A")
# print(tup.count("A"))

#lst = ["C","D","A","A","B","B","A"]
#lst.sort()
#print(lst)

#LECTURE 4

# dict = {
#     "name" : "hanoof",
#     "cgpa" : 9.6,
#     "marks" : [87,96,74]
# }
# print(dict)

# info = {
#     "name" : "hanoof",
#     "subjects" : ["linux","sql","git","python"],
#     "age" : 21,
#     "is_Adult" : True,
#     "topics" : ["dict", "set"]
# }
# info["name"] = "hanoof_buchh"
# print(info.get("age"))

# set_1 = {1,2,3,4,5}
# set_2 = {3,4,5,6,7,8,9,10}
# print(set_1.union(set_2))
# print(set_1.intersection(set_2))

# dictionary = {
#     "table" : ["a piece of furniture","list of facts and figures"],
#     "cat" : "a small animal"

# }
# print(dictionary)
#You are given a list of subjects for students.Assume 1 classroom is required for 1 subject. How many classrooms are needed by all studemnts?
# subjects = {"python","java","c++","python","javascript","java","python","java","c++","c"}
# print("classroom needed: ",len(subjects))
#WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary and add one by one. Use subject name as key and marks as value
# dictionary = {}
# x = int(input("enter phy: "))
# dictionary.update({"phy" : x})
# y = int(input("enter chem: "))
# dictionary.update({"chem" : y})
# z = int(input("enter math: "))
# dictionary.update({"math" : z})
# print(dictionary)

# i = 0
# while i<=10:
#     print("Hello!")
#     i += 1
#     print(i)

#loops
#Print numbers from 1 to 100
# i = 1
# while i<=100:
#     print(i)
#     i+=1

#Print numbers from 100 to 1
# i = 100
# while i>=1:
#     print(i)
#     i-=1
#Print the multiplication table of a number n
# n = int(input("Enter the number: "))
# i = 1
# while i<=10:
#     print(n*i)
#     i+=1

#Print the elements of the following list using a loop:
#[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# numbers = [1,4,9,16,25,36,49,64,81,100]
# i = 0
# while i<len(numbers):
#      print(numbers[i])
#      i+=1

#Search for a number x in this tuple using loop:
#(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# i = 0
# x = int(input("enter the number you want to  find: "))
# while i<len(num):
#     if(num[i]==x):
#         print("found at index",i)
#     else:
#         print("finding...")
#     i+=1
# print("end of loop")
# print 1-10 using loops except 5
# i = 1
# while i <=10:
#     if i==5:
#         i+=1
#         continue
#     print(i)
#     i+=1
#WAP to print odd numbers for 1-10
# i = 1
# while i <=10:
#     if i%2==0:
#         i+=1
#         continue
#     print(i)
#     i+=1

# num = [1,4,9,16,25,36,49,64,81,100]
# for val in num:
#     print(val)

# num = (2,4,5,6,7,8,6,5,5,5,4)
# for val in num:
#     print(val)

# num = {2,4,5,6,7,8,6,5,5,5,4}
# for val in num:
#     print(val)

# str = "Hanoof Buchh"
# for chr in str:
#     print(chr)

# x = int(input("enter number: "))
# num = [1,4,9,16,25,36,49,64,81,100]
# for val in num:
#     if(val==x):
#         print("number found",x)
#         continue
#     print(val)

#Print numbers from 1 to 100
# for i in range(1,100):
#     print(i)

# Print numbers from 100 to 1
# for i in range(100,0,-1):
#     print(i)

# Print the multiplication table of a number n
# n = int(input("Enter number: "))
# for i in range(1,11):
#     print(n*i)

#WAP to find the sum of first n numbers. (using while)

# n = int(input("Enter number: "))
# sum = 0
# i = 1
# while i<=n:
#     sum +=i
#     i+=1
# print("the sum is: ",sum)

# n = int(input("Enter number: "))
# sum = 0
# for i in range(n+1):
#     sum +=i
# print("the sum is: ",sum)    

#WAP to find the factorial of first n numbers
# n = int(input("Enter number: "))
# fact = 1
# for i in range(1,n+1):
#     fact*=i
# print("factorial is: ",fact)

# n = int(input("Enter number: "))
# fact = 1
# i = 1
# while i<=n:
#     fact*=i
#     i+=1
# print("factorial is: ",fact)

# def cal_sum(a,b):
#     sum = a+b
#     print(sum)

# def cal_mul(a,b):
#     mul = a*b
#     print(mul)
#     return mul

# def cal_div(a,b):
#     div = a/b
#     print(div)
#     return div

# def cal_sub(a,b):
#     sub = a-b
#     print(sub)
#     return sub

# cal_mul(5,5)
# cal_sum(5,5)
# cal_sub(5,5)
# cal_div(5,5)

# average of 3 numbers
# def cal_avg(a,b,c):
#     sum = a+b+c
#     avg = sum/3
#     return avg
# num_1 = int(input("Enter first num: "))
# num_2 = int(input("Enter second num: "))
# num_3 = int(input("Enter third num: "))
# average = cal_avg(num_1,num_2,num_3)
# print("the average is: ",average)
 #WAF to print the length of a list
#def print_list_len(my_list):
#    print(len(my_list))
#list = [1,2,3,4,5,6,7,8,9,10]
#print_list_len(list)

# WAF to print the elements of a list in a single line
# cities = ["gurgaon","rohtak","srinagar","mohali","delhi"]
# heroes = ["superman","ironman","thor","hulk","antman","spiderman"]

# def print_elements(list):
#     for i in list:
#         print(i,end=" ")

# print_elements(cities)
# print_elements(heroes)

#WAF to find the factorial of n

#def fact(n):
#    fact = 1
#    for i in range(1,n+1):
#        fact*=i
#    return fact

#n = int(input("Enter number: "))
#result = fact(n)
#print("factorial is: ",result)

# WAF to convert USD to INR.
# def converter(usd_val):
#     inr_val = usd_val * 86.43
#     return inr_val

# a = int(input("Enter USD: "))
# result = converter(a)
# print(a,"USD =",result,"INR")

# def number(num):
#     if num % 2 ==0:
#         return"EVEN"
#     else:
#         return"ODD"
    
# n = int(input("enter number: "))
# print("the number is",number(n))

# def show(n):
#     if n==0:
#         return
#     print(n)
#     show(n-1)

# show(5)

# # write a recursive function to find the factorial of a number
# def fact(n):
#     if (n==1 or n==0):
#         return 1
#     return fact (n-1) * n

# print(fact(4))

# Write a recursive function to calculate the sum of first n natural numbers.
# def sum(n):
#     if(n==0):
#         return 0
#     return sum(n-1)+ n

# print(sum(5))
# Write a recursive function to print all the elements in a list. (hint: use list and index as parameters)
#def print_list(list,idx=0):
#    if (idx == len(list)):
#        return
#    print(list[idx])
#    print_list(list,idx+1)

#fruits = ["mango","grapes","banana","apple","guava","orange","peach","lichi"]
#print_list(fruits)

# f = open("data.txt","r")
# data = f.read()
# print(data)
# f = open("demo.txt","a")
# data = f.write("\nI play cricket as well")
# print(data)

# with open("demo.txt","r") as f:
#     data = f.read()
#     print(data)

# with open("demo.txt","w") as f:
#     data = f.write("new data")
#     print(data)

# Deleting a file
# open("sample.txt","w") 
# import os
# os.remove("sample.txt")

#Create a new file "practice.txt" using python. Add the following data in it:
# Hi everyone
# we are learning File I/O
# using java.
# I like programming in java

# f = open("practice.txt","w")
# data = f.write("Hi everyone\n we are learning File I/O\n using java.\n I like programming in java ")
# f.close()
# Write a function that replaces all occurence of "java" with "python"
# with open("practice.txt","r") as f:
#     data = f.read()
#     new_data = data.replace("java","python")
#     print(new_data)
# with open("practice.txt","w") as f:
#     f.write(new_data)

# Search if the word learning exists in the file or not
# def check_for_word():

#     word = "learning"
#     with open("practice.txt","r") as f:
#         data = f.read()
#         if (word in data):
#             print("found")
#         else:
#             print("not found")
# check_for_word()
# WAF to find in which line of the file does word "learning" occur first. Print -1 if word not found
# def check_for_line():
#     word = "learning"
#     line_no = 1
#     data = True
#     with open("practice.txt","r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no +=1
            
#     return -1
# print(check_for_line())

# From a file containing numbers separated by commas, print the count of even numbers.
# count = 0
# with open("practice.txt","r") as f:
#     data = f.read()
#     nums  = data.split(",")
#     for val in nums:
#         if(int(val) % 2 ==0):
#             count +=1
# print(count)
        
# OOPS 

# class Student():
#     name = "Hanoof"

# s1 = Student()
# print(s1.name)

# s2 = Student()
# print(s2.name)

# class Car():
#     color = "white"
#     brand = "mercedes"

# s1 = Car()
# print(s1.color)
# print(s1.brand)

# class Student():
#     #default constructer
#     def __init__(self):
#         pass
#     #parametrized constructer
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student in database")
# s1 = Student("Hanoof",92)
# print(s1.name)
# print(s1.marks)
       
# s2 = Student("Hadiya",99)
# print(s2.name)
# print(s2.marks)

#Class & Instance Attributes

# class Student():
#     College = "CGC LANDRAN"  #Class Attribute
#     def __init__(self,name,marks):
#         self.name = name     #Object Attribute
#         self.marks = marks   #Object Attribute
# s1 = Student("Hanoof",91)
# s2 = Student("Ashaz",94)
# print(s1.name,s1.marks)
# print(s2.name,s2.marks)
# print(Student.College)

#Method
# class Student():
#     def __init__(self,fullname):
#         self.name = fullname
#     def hello(self):
#         print("hello",self.name)

# s1 = Student("Hanoof")
# s1.hello()

#Create student class that takes name and marks of 3 subjects as arguments in constructor.
# Then create a method to print the average

# class Student():
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hi,",self.name,"your avg score is",sum/3)

# s1 = Student("Hanoof",[96,86,91])
# s1.get_avg()
            
# Static Methods
# Methods that don't use the self parameter(work at class level)

# class Student():
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

#     @staticmethod      
#     def hello():           #Self method
#         print("hello")

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum = sum + val
#         print("hi",self.name,"your average score is: ",sum/3)

# s1 = Student("hanoof",[91,84,89])
# s1.get_avg()
# s1.hello()

#Abstraction
#Hiding the implementation details of a class and only showing the essential features to the user.
# class Car():
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False
#     def start(self):
#         self.acc = True
#         self.clutch = True
#         print("Car has started.....")

# s = Car()
# s.start()

# Create Account class with 2 attributes - balance and account no.
# Create methods for debit, credit and printing the balance.

# class Account():
#     def __init__(self,bal,acc):
#         self.balance = bal
#         self.account_no = acc
#     def debit(self,amount):
#         self.balance = self.balance - amount
#         print("Rs",amount,"was Debited.")
#         print("Current balance",self.get_balance())

#     def credit(self,amount):
#         self.balance = self.balance + amount
#         print("Rs",amount,"was Credited.")
#         print("Current balance",self.get_balance())
#     def get_balance(self):
#         return self.balance

# acc1 = Account(15500,1234)
# acc1.debit(500)
# acc1.credit(1000)
# print(acc1.account_no)

# del keyword

# class Student():
#     def __init__(self,name):
#         self.name = name

# s1 = Student("Hanoof")
# print(s1.name)
# del s1
# print(s1.name)

# Private (like) attributes and methods

# class Account():
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass     #private attribute
#     def get_pass(self):
#         print(self.__acc_pass)
        
# s1 = Account(1234,"abcd")
# print(s1.acc_no)
# print(s1.get_pass())

# class Person():
#     __name = "Anonymous"

#     def __hello(self):      #private method
#         print("hello person")

#     def welcome(self):
#         self.__hello()
#         print(self.__name)

# p1 = Person()
# print(p1.welcome())

# INHERITANCE

# class Car():
#     @staticmethod
#     def start():
#         print("car started....")
#     @staticmethod
#     def stop():
#         print("car stopped....")

# class ToyotaCar(Car):
#     def __init__(self,name):
#         self.name = name
# c1 = ToyotaCar("Fortuner")
# c2 = ToyotaCar("Innova")
# print(c1.name)
# c1.start()
# c1.stop()
# print(c2.name)
# c2.start()
# c2.stop()

# SUPER METHOD
# class Car():
#     def __init__(self,type):
#         self.type = type
#     @staticmethod
#     def start():
#         print("car started....")
#     @staticmethod
#     def stop():
#         print("car stopped....")

# class Toyotacar(Car):
#     def __init__(self,name,type):
#         self.name = name
#         super().__init__(type)
#         super().start()
#         super().stop()
# c1 = Toyotacar("Fortuner","deisel")
# print(c1.name)
# print(c1.type)
  
# CLASS METHOD
# class Person:
#     name = "Anonymous"
#     @classmethod
#     def change_name(self,name):
#         self.name = name

# n1 = Person()
# n1.change_name("hanoof")
# print(n1.name)
# print(Person.name)

# PROPERTY METHOD
# class Student():
#     def __init__(self,phy,chem,math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
        
#     @property
#     def percentage(self):
#         return str((self.phy+self.chem+self.math)/3) + "%"

# s1 = Student(98,87,84)
# print (s1.percentage)
# s1.math = 92
# print(s1.percentage)

# POLYMORPHISM

# class Complex:
#     def __init__(self,real,img):
#         self.real = real
#         self.img = img

#     def shownumber(self):
#         print(self.real,"i","+",self.img,"j")

#     def __add__(self,num2):              #dunder function
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return Complex(newReal,newImg)
    
#     def __sub__(self,num2):              #dunder function
#         newReal = self.real - num2.real
#         newImg = self.img - num2.img
#         return Complex(newReal,newImg)
    
# n1 = Complex(2,4)
# n1.shownumber()
# n2 = Complex(5,6)
# n2.shownumber()
# n3 = n1 + n2
# n3.shownumber()
# n4 = n1 - n2
# n4.shownumber()

# Define a Circle class to create a class with radius r using construstor.
# Define an area() method of the class which calculates the area of the circle.
# Define a perimeter method of a class which allows you to calculate the perimeter of the circle.

# class Circle:
#     def __init__(self,radius):
#         self.radius = radius
#         print("radius of a circle: ",radius)

#     def area(self):
#         area = (22/7)*self.radius**2
#         print("The area of the circle is: ",area)

#     def parameter(self):
#         parameter = 2*(22/7)*self.radius
#         print("The parameter of the circle is: ",parameter)

# c1 = Circle(21)
# c1.area()
# c1.parameter()

# Define an employee class with attributes role,department and salary. This class also has a showDetail() method.
# create an engineer class that inherits the property from employee and has attributes: name & age

# class Employee:
#     def __init__(self,role,department,salary):
#         self.role = role
#         self.department = department
#         self.salary = salary

#     def showDetails(self):
#         print("Role = ",self.role)
#         print("Department = ",self.department)
#         print("Salary = ",self.salary)

# class Engineer(Employee):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer","IT","50000")

# e2 = Engineer("Hanoof",21)
# e2.showDetails()

# Create a class called order which stores item and its price.
# use dunder function __gt__() to convey that:
# order1 > order2 if price of order1 > order2

# class Order:
#     def __init__(self,item,price):
#         self.item = item
#         self.price = price

#     def __gt__(self,odr2):
#         return self.price > odr2.price
    
# odr1 = Order("Apple",50)
# odr2 = Order("Banana",20)
# print(odr1>odr2)
    
# WAP to develop a game called guess the number

# import random
# target = random.randint(1,100)

# while True:
#     user_choice = input("Guess the number or Quit(Q): ")
#     if (user_choice == "Q"):
#         break
#     user_choice = int(user_choice)
#     if(user_choice == target):    
#         print("You have guessed the correct number....")
#         break
#     elif(user_choice > target):
#         print("number too large \nchoose smaller number")
#     else:
#         print("number too small \nchoose bigger number")
# print("----GAME ENDED----")

# create a random password generator

# import random
# import string

# char = string.ascii_letters + string.digits + string.punctuation

# pass_len = 12
# password = ""

#list comprehension [function for i in range(n)]
# password = "".join([(random.choice(char)) for i in range(pass_len)])
# print(password)

# for i in range (pass_len):
#     password += random.choice(char)
# print("your random password is: ",password)

