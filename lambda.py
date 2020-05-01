#maping

list1=[1,2,3,4]
print(list(map(lambda a:a+3,list1)))

n=[3,4,5,6]
print(list(map(lambda b:b*2 ,n)))

a=lambda a,b:a if a<b else b
print(a(4,6))

def mysum(n):
    return lambda a,b: n+2 if a>b else n-1
cond=mysum(3)
print(cond(2,3))

#filter

z=[22,21,43,56,78,66,11]
print(list(filter(lambda x: (x%2 != 0) , z)))

x=[1,2,3,4]
print(list(filter(lambda a:a>2 , x)))

#reduce

from functools import reduce
num=[2,3,4,5,7]
print(reduce(lambda a,b: a*b , num))