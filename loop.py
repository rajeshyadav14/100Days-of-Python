
# Print numbers from 1 to 10 
'''
count = int(input("Enter Number: "))
i = 1

while i <= count:
    print(f"{i} Hello Hidden")
    i += 1
'''
# Print Reverse from 10 to 1 
'''
count = int(input("Enter Number: "))
i = count

while i >= 1:
    print(f"{i} Hello World!")
    i -= 1

'''

#Odd Number
'''
n = int(input("Enter number: "))

i = n 

while i >= 1:
    if i % 2 != 0:
        print(i)
    i -= 1
'''
'''
n = int(input("Enter Number: "))

i = n - (n % 2 == 0)
while i >= n:
    print(i)
    i -= 2

'''

#Reverse even numbers (without using if)

n = int(input("Enter Number: "))

i = n - (n % 2)

while i >= 2:
    print(i)
    i -= 2

