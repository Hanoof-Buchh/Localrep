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