
#Take a name as input and print:


userName = input("Enter Name:")
print("Hello",userName,"Welcome to Hacker Lobby!")


#Take two numbers as input and print their sum

num1 = int(input("Enter Number1: "))
num2 = int(input("Enter Number2: "))
total = num1 + num2 
print("Sum of num1 and num2 is:",total)



#Take age as input and print:

userAge = int(input("Enter Age: "))
print("You are",userAge,"years old.")


#Take a number as input and print its square


sqr = int(input("Enter a Number for getting Square: "))
res = sqr ** 2 
print("Square of",sqr,"is",res)



#Take temperature in Celsius and convert it to Fahrenheit

celsius = float(input("Enter a Celsius: "))
fahrenheit = celsius * 9/5 + 32
print("Your are Celsius is",celsius,"after convert into fahrenheit is",fahrenheit)



#Take two numbers (as input) and print: Sum, Difference, Product 

a = float(input("Enter Number 1: "))
b = float(input("Enter Number 2: "))
print(f"Sum:{a+b}")
print(f"Difference:{a-b}")
print(f"Product:{a*b}")


#Take a decimal number and convert it to an integer, then print it

num = float(input("Enter a Decimal Number: "))
res = round(num)
print(f"After Converting Decimal to Interger Value is: {res}")


#Take name and birth year → calculate age

name = input("Enter name: ")
birthYear = int(input("Enter Birth Year: "))
currentYear = int(input("Enter Current Year: "))
currentAge = currentYear - birthYear

print(f"Your Name is:{name}")
print(f"Your Current Age is:{currentAge}")



#Take 3 numbers and print their average

num11 = float(input("Enter Number 1: "))
num12 = float(input("Enter Number 2: "))
num13 = float(input("Enter Number 3: "))
average = (num11+num12+num13)/3
print(f"Average:{average}")

#Take length and width → print area of rectangle

length = float(input("Enter length: "))
width = float(input("Enter Width: "))
area = length * width
print(f"Area of Rectange is {area}")

#Take a number and print:
#Double: __
#Triple: __

num14 = float(input("Enter a number: "))

print(f"Double: {num14 * 2}")
print(f"Triple: {num14 * 3}")