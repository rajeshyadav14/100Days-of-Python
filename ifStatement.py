
#1. Check if a number is: Positive, Negative, Zero

'''
number = int(input("Enter Number: "))
if number > 0:
    print(f"{number} is Positive")
elif number < 0:
    print(f"{number} is Negative")
else:
    print("Number is Zero")
'''

#2. Check if a number is: Even, Odd
'''
num = int(input("Enter Number: "))

if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")
'''

#3. Take age and print: Eligible to vote (age ≥ 18), Not eligible
'''
age = int(input("Enter Age: "))

if age >= 18:
    print(f"Your Age is {age} and you are Eligible to vote.")
else:
    print(f"You are {age} years old and not eligible to vote.")
'''

#4. Largest of 2 Numbers
'''
num1 = float(input("Enter Number 1: "))
num2 = float(input("Enter Number 2: "))

if num1 > num2:
    print(f"{num1} is Largest Number.")
elif num2 > num1:
    print(f"{num2} is Largest Number.")
else:
    print(f"Both {num1} and {num2} are equal.")
'''

#5. Largest of 3 Numbers
'''
num1 = float(input("Enter Number 1: "))
num2 = float(input("Enter Number 2: "))
num3 = float(input("Enter Number 3: "))

if num1 == num2 == num3:
    print("All numbers are equal")
elif num1 >= num2 and num1 >= num3:
    print(f"{num1} is the largest number")
elif num2 >= num1 and num2 >= num3:
    print(f"{num2} is the largest number")
else:
    print(f"{num3} is the largest number")
'''

#6. Take marks as input and print grade: ≥ 90 → Grade A, ≥ 70 → Grade B, ≥ 50 → Grade C, < 50 → Fail
'''
marks = int(input("Enter Marks: "))

if marks >= 90:
    print(f"Grade A: {marks}")
elif marks >= 70:
    print(f"Grade B: {marks}")
elif marks >= 50:
    print(f"Grade C: {marks}")
else:
    print(f"Fail: {marks}")
'''

#7. Simple Calculator
'''
num1 = float(input("Enter Number 1: "))
num2 = float(input("Enter Number 2: "))

operator = input("Select Operator: ")

if operator == "+": 
    result = num1 + num2
    print(f"{num1} {operator} {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} {operator} {num2} = {result} ")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} {operator} {num2} = {result}")
elif operator == "/":
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        result = num1 / num2
        print(f"{num1} {operator} {num2} = {result}")   
else:
    print("Invalid Operator")
'''


#8. Divisibility Checker : Divisible by both 3 and 5 , Only by 3 ,Only by 5, Not divisible

num = int(input("Enter Number: "))

if num % 3 == 0 and num % 5 == 0:
    print(f"Divisible by both 3 and 5: {num}")
elif num % 3 == 0:
    print(f"Only Divisble by 3: {num}")
elif num % 5 == 0:
    print(f"Only Divisible by 5: {num}")
else:
    print(f"Not Divisible by 3 and 5: {num}")
