from sympy import symbols, Eq, solve

"""

2x+3y=13
x-2y=-4

"""

x, y = symbols('x y')

equations = (
    Eq(2 * x + 3 * y - 13, 0),
    Eq(x - 2 * y + 4, 0)
)

result = solve(equations,(x,y))

print(result)
