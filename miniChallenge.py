'''
Build a simple bill generator:
Take item name
Take price
Take quantity
'''
#Bill Generator 
'''
item = input("Enter Item Name: ")
quantity = int(input("No of Items: "))
price = float(input("Enter Price Per Items: "))
total_price = quantity * price 

print("\n---------- Bill ----------")
print(f"Item: {item}")
print(f"Quantity: {quantity}")
print(f"price per item: {price}")
print(f"Total Amount: {total_price}")
'''
#Take two numbers from user and swap them.

'''
num1 = float(input("Enter Number 1: "))
num2 = float(input("Enter Number 2: "))

print(f"Before Swaping : {num1} , {num2}")
swap = num1 
num1 = num2 
num2 = swap
print(f"After Swaping: {num1} , {num2}")

print(num1)
print(num2)
'''

#Take seconds as input → convert into: Minutes, Hours

second = int(input("Enter Second: "))
minute = (second // 60)
hours =  (second // 3600)

print(f"{hours}H {minute}M {second}S")