
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

