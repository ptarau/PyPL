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
