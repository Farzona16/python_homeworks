### Number Data Type Questions:

# 1. Create a program that takes a float number as input and rounds it to 2 decimal places.
# my_num=float(input("enter a float number: "))
# print(round(my_num,2))

# 2. Write a Python file that asks for three numbers and outputs the largest and smallest
# a=float(input("a= "))
# b=float(input("b= "))
# c=float(input("c= "))
# if a>=b and a>=c:
#     print(a)
# elif b>=a and b>=c:
#     print(b)
# else: print(c)

# 3. Create a program that converts kilometers to meters and centimeters.
# distance=float(input("masofani kiriting kmda: "))
# in_meter=float(distance*1000)
# in_cm=float(distance*100000)
# print(f"our distance is {in_meter}m or {in_cm}cm")

# 4. Write a program that takes two numbers and prints out the result of integer division and theremainder.
# a=float(input("a= "))
# b=float(input("b= "))
# integer_division=a//b
# remainder=a%b
# print(f"Integer division is {integer_division} and remainder is {remainder}")

# 5. Make a program that converts a given Celsius temperature to Fahrenheit.
# temperature_in_celcius=float(input("enter the temperature in celcius: "))
# temp_in_fahrenheit=(temperature_in_celcius*9/5)+32
# print(f"Altered temperature is {temp_in_fahrenheit}")

# 6. Create a program that accepts a number and returns the last digit of that number.
# number=float(input("enter your number: "))
# last_digit=int(number%10)
# print(last_digit)

# 7. Create a program that takes a number and checks if it’s e
# import math
# my_num=float(input("enter your number: "))
# if my_num==math.e:
#     print(f"It is equal with e")
# else:
#     print(f"It is not equal with e ")


### String Questions:

# 1. Create a program to ask name and year of birth from user and tell them their age.
# name=input("what is your name: ")
# year=int(input("which year you was born: "))
# age=2024-year
# print(f"Hello {name}! You are {age} years old.")

# 2. Extract car names from this text:
# txt = 'LMaasleitbtui'
#-----------ISHLOLMADIM--------------


# 3. Write a Python program to:
#    - Take a string input from the user.
#    - Print the length of the string.
#    - Convert the string to uppercase and lowercase.
# text=input("enter the text: ")
# length=len(text)
# print(f"{length}")
# print(text.upper())
# print(text.lower())

# 4. Write a Python program to check if a given string is `palindrome` or not.
#--------------ISHLOLMADIM--------------

# > What is a Palindrome String? A string is called a palindrome if the reverse of the string is the same as the original one. Example: “madam”, “racecar”, “12321”.

# 5. Write a program that counts the number of vowels and consonants in a given string.
#--------------Ishlolmadim------------

# 6. Write a Python program to check if one string contains another.
# def contains(main,sub):
#     return sub in main
# main=input("enter main string: ")
# sub=input("enter sub string: ")
# if  contains(main,sub):
#     print(f"{sub} is in the {main}")
# else: print(f"{sub} isn\`t in {main}")

# 7. Ask the user to input a sentence and a word to replace. Replace that word with another word provided by the user.  
# Example:  
#    - Input sentence: "I love apples."  
#    - Replace: "apples"  
#    - With: "oranges"  
#    - Output: "I love oranges."
# sentence=input("enter your sentence: ")
# which_word=input("enter your: ")
# another_word=input("enter your word to replace: ")
# print(sentence.replace(which_word,another_word))

# 8. Write a program that asks the user for a string and prints the first and last characters of the string.  
# text=input("enter your text: ")
# first=text[0]
# last=text[-1]
# print(f"{first} and {last}")

# 9. Ask the user for a string and print the reversed version of it.
# my_text=input("enter your text: ")
# reversed_text=my_text[::-1]
# print(reversed_text)

# 10. Write a program that asks the user for a sentence and prints the number of words in it.
# mytext=input("enter your sentence: ")
# number_of_space=mytext.split()  
# number_of_words=len(number_of_space)
# print(number_of_words)

# 11. Write a program to check if a string contains any digits.  
# def function(string):
#     return any(char.isdigit() for char in string)
# my_str=input("enter your string: ")
# if function(my_str):
#     print("these sentence contains digit")
# else:print("these sentence doesnt contain any digit")


# 12. Write a program that takes a list of words and joins them into a single string, separated by a character (e.g., `-` or `,`).  

# 13. Ask the user for a string and remove all spaces from it.  

# 14. Write a program to ask for two strings and check if they are equal or not.  

# 15. Ask the user for a sentence and create an acronym from the first letters of each word.  
#     Example:  
#     - Input: "World Health Organization"  
#     - Output: "WHO"  

# 16. Write a program that asks the user for a string and a character, then removes all occurrences of that character from the string.  

# 17. Ask the user for a string and replace all the vowels with a symbol (e.g., `*`).  

# 18. Write a program that checks if a string starts with one word and ends with another.  
#     Example:  
#     - Input: "Python is fun!"  
#     - Starts with: "Python"  
#     - Ends with: "fun!"  


### Boolean Data Type Questions:
# 1. Write a program that accepts a username and password and checks if both are not empty.
# username=input("enter your username: ")
# password=input("enter your password: ")
# if username !="" and password !="":
#     print("checked!")
# else:print("mustn\`t be empty!")

# 2. Create a program that checks if two numbers are equal and outputs a message if they are.
# first_num=float(input("first number: "))
# second_num=float(input("second number: "))
# if first_num==second_num:
#     print("they are equal")

# 3. Write a program that checks if a number is positive and even.
# my_num=int(input("enter positive and even number: "))
# if my_num%2==0 and my_num>0:
#     print("it`s even and positive")
# else: print("try again")

# 4. Write a program that takes three numbers and checks if all of them are different.
# first=float(input("enter first number: "))
# second=float(input("enter second number: "))
# third=float(input("enter third number: "))
# if first!=second and first!=third and second!=third:
#     print("Good!")
# else:print("try again")

# 5. Create a program that accepts two strings and checks if they have the same length.
# string_one=input("enter your 1st string: ")
# string_two=input("enter your second string: ")
# length_1=len(string_one)
# length_2=len(string_two)
# if length_1==length_2:
#     print("they`re lens are same")
# else:print("they`re lens are not same")

# 6. Create a program that accepts a number and checks if it’s divisible by both 3 and 5.
# my_num=int(input("enter the number: "))
# if my_num%3==0 and my_num%5==0:
#     print("divisible to both of them")
# else:print("try again")

# 7. Write a program that checks if the sum of two numbers is greater than 50.
# a=float(input("a: "))
# b=float(input("b: "))
# sum_of_them=a+b
# if sum_of_them>50:
#     print("their sum is greater than 50")
# else:print("their sum is not greater than 50")

#8. Create a program that checks if a given number is between 10 and 20 (inclusive)
# a=float(input("enter the number: "))
# if a>=10 and a<=20:
#     print("it`s accepted")
# else: print("it couldn`t be accepted")