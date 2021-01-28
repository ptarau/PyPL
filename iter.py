from itertools import *

def take(n,g) :
  for i,x in enumerate(g) :
    if i >= n: break
    yield x

def drop(n,g) :
  for i,x in enumerate(g) :
    if i < n: continue
    yield x


for x in take(10,cycle('abcd')) : print(x)


print(list(drop(3,range(10))))


print(tuple(chain([1,2,3],[4,5])))

def myprint(*args) :
  print('DEBUG:',*args)

