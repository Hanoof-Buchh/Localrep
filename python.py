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