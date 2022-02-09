from itertools import *

# do this first: pip3 install more-itertools
from more_itertools import *

t1 = take(3, [1, 2, 3, 4, 5, 6])
print('t1', t1)

t2 = take(7, count(100, 3))
print('t2', t2)

t3 = take(40, cycle([100, 200, 300]))
print('t3', t3)


def plus(x, y):
    return x + y


t4 = list(accumulate([2, 4, 6, 11, 20], plus))
print('t4', t4)

t5 = list(chain(range(7), "abcd", ['hello', 'bye']))
print('t5', t5)


def from_file(fname):
    with open(fname, 'r') as f:
        for l in f.readlines():
            yield l[:-1]


t6 = list(from_file('generators.py'))
print(t6)

s1 = [1, 2, 3, 4]
s2 = [10, 20, 30, 40]

t7 = list(map(plus, s1, s2))
print(t7)


def unzip(xs):
    yield from zip(*xs)


zs = list(zip(s1, s2))
ls = list(zip(*zs))

s3 = [0, 1, 2, 3, 40, 5, 6, 7, 8, 9, 10, 11]


def small(x):
    return x < 8


t8 = list(takewhile(small, s3))
print('t8', t8)

t9 = list(dropwhile(small, s3))
print('t9', t9)

t8a = list(takewhile(lambda x: x < 8, s3))
print('t8a', t8a)

t9a = list(dropwhile(lambda x: x < 8, s3))
print('t9a', t9a)

i0 = cycle("abc")

i1 = from_file('generators.py')

i2 = tee(cycle("abc"))


def sq(n):
    """
      returns square roots of
      first n numbers
    """
    for x in range(n):
        yield x ** 2


def min_max(i):
    i1, i2, i3 = tee(i, 3)
    return min(i1), max(i2), sum(i3)


def counts_from():
    i = from_file('generators.py')
    i1, i2 = tee(i)
    return len(list(i1)), list(map(len, i2))


print(counts_from())


def drop(k, xs):
    for _ in range(k):
        next(xs)
    return list(xs)


t11 = nth(from_file('generators.py'), 5)
print('t11', t11)

t12 = list(islice(from_file('generators.py'), 103, 108))
print(t12)

"""
hello
"""


def cprod(xs,ys):
    for x in xs:
        for y in ys:
            yield (x,y)


print(list(cprod("abc",[1,2,3,4])))

print(list(product("ab",[1,2,3],"XY")))


def cpower(xs,n):
    yield from product(iter(xs),repeat=n)


print(list(cpower([0,1],3)))
