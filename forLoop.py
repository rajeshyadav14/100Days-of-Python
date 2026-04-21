
#Write a Program to print numbers taking input from users using a for loop 
'''
n = int(input("Enter Numbers: "))

for i in range(1,n+1):
    print(i , end=" ")
'''

# Print Squares of Numbers from taking input by users 
'''
n = int(input("Enter Numbers: "))

for i in range(1,n+1):
    print(i**2, end=" ")
'''

# Print Even Numbers From taking input by users 
'''
n = int(input("Enter Numbers: "))

for i in range(1,n+1):
    if i % 2==0:
        print(f"{i} is Even Number")

'''

# Print Odd Numbers From taking input by users

''' 
n = int(input("Enter Numbers: "))

for i in range(1,n+1,2):
    print(i, end=" ")
'''

# Write a Program to calculate the sum of number by taking input from users 

'''
n = int(input("Enter Number: "))
total = 0

for i in range (1,n+1):
    total += i 
print(f"Sum is {total}")


n = int(input("Enter Number: "))

total = n * (n + 1) // 2  # input number * total number // divide by 2 

print(f"Sum is {total}")
'''

# Write a program to calculate the sum of the first n even numbers using a mathematical formula.

n = int(input("Enter Number: "))
total = 0
for i in range(1, n+1):
    if i%2==0:
        print(i, end=" " )
        total += i

print("\n",total, end=" ")



