
#Sum of Digit of a Number using While Loop taking input by user
'''
n = int(input("Enter Number: "))

total = 1
while n > 0:
    digit = n % 10
    total *= digit
    n = n // 10
    
print(total)
'''

#Count digits using while
'''
n = int(input("Enter Number: "))
count = 0
 
while n > 0:
    count += 1
    n = n//10
print(count)
'''
'''

n = int(input("Enter Number: "))

if n == 0:
    count = 1
else:
    count = 0
    while n > 0:
        count += 1
        n = n // 10
   

print(count)

'''

#Reverse Number 
'''
n = int(input("Enter Number: "))
n = abs(n) # Handle Negative Number

rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print(rev)
'''

# Palindrome Check 
'''
string = input("Enter Word To Check Palindrome: ")
string = string.upper()
rev = string[::-1]

if rev == string:
    print("Palindrome")
else:
    print("Not a Palindrome")
'''

'''

word = input("Enter Words: ")
word = word.upper()
rev = ""
i = len(word)-1

while i >= 0:
    rev += word[i]
    i -= 1

if rev == word:
    print("Palindrome")
else:
    print("Not a Palindrome")


'''   
   
 # Fibonacci series using while loop
'''
n = int(input("Enter Number: ")) 
prev = 0
curr = 1

while n > 0:
    print(prev,end=" ")
    next = prev + curr
    prev = curr
    curr = next
    n -= 1
   
'''

#Fibonacci Series using while loop with limit

n = int(input("Enter Number: ")) 
prev = 0
curr = 1

while prev <= n:
    print(prev,end=" ")
    next = prev + curr
    prev = curr
    curr = next
   

#Fibonacci without using next variable
'''
n = int(input("Enter Numbers: "))

prev = 0
curr = 1

while n > 0:
    print(prev,end=" ")
    curr = prev + curr
    prev = curr - prev
    n -= 1

'''
