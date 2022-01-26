# What kind of functions we will use?

# Finite Functions: lists(dynamic arrays), sets, frozen sets, dicts

# array/lists

xs=[1,2,3]

print(xs)

x=xs[0]

xs.append(10)
xs[0]=20

print(xs)

print(x)

# dict

d=dict(one=1,two=2)

d1={'one':1,'two':2}

print('d at 2:',d['two'])

for k,v in d.items():
    print('kv:',k,v)

print('one' in d1)
print('nine' in d1)

d['one']=100

print(d)

# strings

s="abc"

# tuples

ts=(1,2,3)

print(ts)

# sets and frozen sets

us={1,2,3}
us.add(0)

vs={2,3,4,5}

print(us & vs)
print(us | vs)

fs=frozenset({1,2,3})
gs=frozenset({2,3,4,5})
print(fs|gs)

hs=frozenset({5,fs,gs,fs,5})
print(hs)


# Built-in and functions fro packages

import numpy as np

npa=np.array([[1,2,3],[10,20,30]])

print(npa)
print(npa.T)

# user defined functions

def myfun(x,y):
    return x*x+x*y

print(myfun(2,3))

def fibo(n) :
    if n<=1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

print(fibo(10))

# Lazy finite (and not finite) functions (generators)

def myrange(f,t):
    i=f
    while i<t:
        yield i
        i+=1

def myloop(i) :
    while True:
        yield i
        i+=1


# Callables: classes and instance as functions

# see symtable.py



