# for picking out random number
import random

print(random.randrange(1, 10))

# for multiple lines initialization
a = "\n this is not my first program" \
    "\n but this is very basic \n"
print(a)

# Checks if the certain phrase is present in the text
txt = "i just had breakfast"
print("fast" in txt)

# format
age = 19
txt = "\n My name is oswa, and I am {}"
print(txt.format(age))

# to highlight any word in the text
txt = "\n i had \"eggs\" in breakfast."
print(txt)

# string methods
a = "oswa"
print(a.upper())
print(a.capitalize())
print(a.lower())
print(a.casefold())
print(a.count("s"))
# encode
txt = "My name is oswå"
x = txt.encode()
print(x)

# list
thislist = ["apple", "banana", "cherry"]
thislist.remove("apple")
del thislist[0]
print(thislist)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
print(list1 + list2)
list1.extend(list2)
print(list1)
list1.append(list2)
print(list1)
list1.extend(list2)
print(list1)

# tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
