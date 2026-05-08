
#factorial
'''
n = int(input("Enter Number: "))

if n < 0:
    print("Factorial not defined")
else:
    factorial = 1
    for i in range(1,n+1):  
        factorial *= i
    print(f"Factorial of {n} is {factorial}")

'''



#Find Vowels 
'''
string = input("Enter Word: ").lower()
vowels = "aeiou"
count = 0

for char in string:
    if char in vowels:
        count += 1

print(count)
'''


# Square Star Pattern 
'''
n = int(input("enter number: "))

for i in range(1, n+1):
    for j in range(1, n+1):
        print("*", end=" ")
    print()

'''

#Half 90 degree star pattern 
'''
n = int(input("enter number: "))

for i in range(1,n+1):
    for j in range(1,i+1):  #1 , i+1=2 (1,2)
        print("#", end=" ")
    print()

'''

#reverse Half 90 degree star pattern 

n = int(input("enter number: "))

for i in range(n+1,0,-1):
    for j in range(i):
        print("*",end= " ")
    print()

