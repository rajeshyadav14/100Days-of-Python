
#Slice 

#You can return a range of characters by using a slice syntax

#Slicing have 3 parameter to use slicing string [Start, Stop, Step]

string = "HiddenxWorld!"

substr1 = string[5:10]
print(substr1)

substr2 = string[:10]
print(substr2)

substr3 = string[3:]
print(substr3)

substr4 = string[:]
print(substr4)

substr5 = string[-2:-1]
print(substr5)

substr6 = string[-9:-3]
print(substr6)

substr7 = string[::-1]
print(substr7)

substr8 = string[5::2].upper()
print(substr8)


text = "Programming"
substr = text[3:7]
print(substr)

substr9 = text[:5:2]
print(substr9)

substr10 = text[::-1]
print(substr10)

substr11 = text[1] + text[3] + text[5] + text[8] + text[10]
print(substr11)

# 1. output: "gram"
# 2. output: "Por"
# 3. output: "gnimmargorP"
# 4. output: "rgaig"