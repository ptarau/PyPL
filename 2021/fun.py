def fibo(n) :
  if n<2 : 
    return 1
  else :
    return fibo(n-2) + fibo(n-1)
  
succ = lambda x : x+1  

fibo1 = lambda x : 1 if x<2 else fibo1 (x-1) + fibo1(x-2)


def fibo2(n) :
  i = 1
  j = 1 
  k=0
  while(k<n) :
    ij=i+j
    i=j
    j=ij
    k+=1
  return i
  
def fibos(n) :  
  def f() :
    i,j = 0,1
    k = 0 
    while(k<n) :
      k+=1
      i,j=j,i+j
      yield i
  return list(f())
  
def fibos1(n) :
   rs=[]
   i,j = 0,1 
   k = 0
   while(k<n) :
     k+=1
     i,j=j,i+j
     rs.append(i)
   return(rs)

def plus(x,y) : return x+y

def mult(x,y) : return x*y

def reduce_with(f,x,xs) :
   r=x
   while xs :
     y=xs.pop()
     r=f(r,y)
   return r

def my_map(f,xs,ys) :
  res=[]
  for i in range(len(xs)) :
    r=f(xs[i],ys[i])
    res.append(r)
  return res


from functools import reduce
from  operator import add,mul


def t1() :
  s=reduce(add,[1,2,3,4],0)
  print(s)
  p=reduce(mul,[1,2,3,4])
  print(p)
  print(sum([1,2,34]))


def cartprod(xs, ys):
  return list((x, y) for x in xs for y in ys)


lc1 = cartprod([1, 2], ['a', 'b', 'c'])
# [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c')]

lc2 = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]


def pythagoras(n):
  for x in range(1, n):
    for y in range(1, n):
      for z in range(1, n):
        if x * x + y * y == z * z:
          yield (x, y, z)


def pythagoras1(n):
  return [(x, y, z) for x in range(1, n)
          for y in range(1, n)
          for z in range(1, n)
          if x * x + y * y == z * z
          ]


def pythagoras2(u):
  for m in range(1, u):
    for n in range(1, m):
      x = m ** 2 - n ** 2
      y = 2 * m * n
      z = m ** 2 + n ** 2
      yield (x, y, z)

# (a-b)^2=a^2-2ab+b^2

'''
>>> for p in pythagoras(20) : print(p)
... 
(3, 4, 5)
(4, 3, 5)
(5, 12, 13)
(6, 8, 10)
(8, 6, 10)
(8, 15, 17)
(9, 12, 15)
(12, 5, 13)
(12, 9, 15)
(15, 8, 17)
'''

# examples of use

print('hello')

print(fibo(11))


def nat_from(n) :
  while(True) :
    yield n
    n+=1

def take(k,g) :
  for i,x in enumerate(g) :
    if i >= k : break
    yield x

def drop(k,g) :
  for i,x in enumerate(g) :
    if i >= k :
      yield x

# implement drop(k,g) :
# drops the first k elements


#t1()
'''
>>> succ(5)
6
>>> (lambda x: x*x)(10)
100
>>> 10*10
100
>>> fibo1(10)
89
>>> fibo(10)
89
>>> fibo2(10)
89
>>> fibos(10)
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
>>> fibos(11)
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> fibos1(10)
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
>>> range(5)
range(0, 5)
>>> range(0,5)
range(0, 5)
>>> list(range(0,5))
[0, 1, 2, 3, 4]
>>> set(range(0,5))
{0, 1, 2, 3, 4}
>>> set([1,2,3,2,1,4])
{1, 2, 3, 4}
>>> set([5,1,2,3,2,1,4,5])
{1, 2, 3, 4, 5}
>>> 

'''

from itertools import *

def take(k,g) :
  for i,x in enumerate(g):
    if i>=k : break
    yield x

def ltake(k,g) :
  return list(take(k,g))

'''

>>> list(accumulate(range(1,10),lambda x,y : x*y))
[1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
>>> chain('ABC', 'DEF')
<itertools.chain object at 0x7fcb3808dcd0>
>>> list(chain('ABC', 'DEF'))
['A', 'B', 'C', 'D', 'E', 'F']
>>> "".join(chain('ABC', 'DEF'))
'ABCDEF'
>>> ";".join(chain('ABC', 'DEF'))
'A;B;C;D;E;F'
>>> dropwhile(lambda x: x<5, [1,4,6,4,1])
<itertools.dropwhile object at 0x7fcb482729b0>
>>> list(dropwhile(lambda x: x<5, [1,4,6,4,1]))
>>>
>>> >>> list(dropwhile(lambda x: x<5, [1,4,6,4,1])
>>> list(takewhile(lambda x: x<5, [1,4,6,4,1]))
[1, 4]
>>> >>> list(filter(lambda x: x<5, [1,4,6,4,1]))
[1, 4, 4, 1]
'''

def grouping(data) :
  groups = []
  uniquekeys = []
  def keyfunc(x) :
   return x

  data = sorted(data, key=keyfunc)
  for k, g in groupby(data, keyfunc):
    groups.append(list(g))      # Store group iterator as a list
    uniquekeys.append(k)
  return groups,  uniquekeys

data = {0:'a',1:'b',0:'c',1:'d'}

print(grouping(data))
