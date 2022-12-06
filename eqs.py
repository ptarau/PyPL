from sympy import symbols, Eq, solve
from random import randint,seed
import random

seed(13)

"""

2x+3y=13
x-2y=-4

"""

x, y = symbols('x y')

equations = (
    Eq(2 * x + 3 * y - 13, 0),
    Eq(x - 2 * y + 4, 0)
)

result = solve(equations, (x, y))


# print(result)


def oneeq(x, y, m):
    while True:
        a = randint(-m, m)
        b = randint(-m, m)
        if a != 0 and b != 0:
            c = a * x + b * y
            r = f'{a}x+{b}y={c}'
            r = r.replace('+-', '-')
            r = r.replace('1x', 'x')
            r = r.replace('1y', 'y')
            return r


def onepair(m):
    x = randint(-m, m)
    y = randint(-m, m)
    eq1 = oneeq(x, y, m)
    while True:
       eq2 = oneeq(x, y, m)
       if eq1!=eq2:
           break
    return (eq1+ '\n'+ eq2), x, y


def eqgen(k=10, m=5, sols=0):
    with open('eqs.txt','w') as f:
      for i in range(k):
        eqs, x,y = onepair(m)
        print(eqs,file=f)
        if sols: print(f'           solution: x={x}, y={y}',file=f)
        print(file=f)


eqgen()
