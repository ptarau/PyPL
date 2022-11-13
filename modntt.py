from operator import *


def gen_tt(op, n):
    m=2**n
    for i in range(m):
        for j in range(m):
            si = bin(i)[2:].rjust(n, '0')
            sj = bin(j)[2:].rjust(n, '0')
            o = (op(i, j) % n)
            so = bin(o)[2:].rjust(n, '0')

            print(si, sj, so)
    print()


gen_tt(add, 3)
gen_tt(mul, 2)
