#1

def div(a,b):
    print (a/b)

def smart_div(div):

    def inner(a,b):
        if a<b:
            a,b=b,a
            return div(a,b)
    return inner

div=smart_div(div)
div(2,8)

#2

def myfunction(a,b):
    print (a+b)
def mydecorator(myfunction):
   def wrapper(a,b):
       a=a+2
       b=b+2
       return myfunction(a,b)
   return wrapper
myfunction=mydecorator(myfunction)
myfunction(2,3)

#3

def scream():
    print("scream")
from datetime import datetime
def not_during_the_night_time(scream):
     def wrapper():
        if 8<=datetime.now().hour<23:
           scream()
        else:
            print(" hush neighbours are sleeping ")
     return wrapper

scream=not_during_the_night_time(scream)
scream()

#4

import time
import math
# decorator to calculate duration
# taken by any function.
def calculate_time(func):
    # added arguments inside the inner1,
    # if function takes any arguments,
    # can be added like this.
    def inner1(a):
        # storing time before function execution
        print("started")

        begin = time.time()

        func(a)

        # storing time after function execution
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)

    return inner1
# this can be added to any function present,
# in this case to calculate a factorial
@calculate_time
def factorial(num):
    # sleep 2 seconds because it takes very less time
    # so that you can see the actual difference
    time.sleep(1)
    print(math.factorial(num))

# calling the function.
factorial(10)