import functools

# s,k combinators, lambdas and more

s = lambda f: lambda g: lambda x: (f)(x)((g)(x))
k = lambda x: lambda y: x
i = lambda x : (s)(k)(k)
# i = lambda x : x

# Rosser's x combinator in terms of s,k
x = lambda f: (f)(k)(s)(k)

# once again, s_,k_ in terms of Rosser's x combinator
s_ = (x)((x)(x))
k_ = ((x)(x))(x)
i_ = i = (s_)(k_)(k_)

plus = lambda x: lambda y: x+y
succ = lambda x : x+1

# the y recursion combinator
y = lambda f: (lambda x: x(x))(lambda z: f(lambda u: z(z)(u)))

# looping in Python
y_ =(s)((k)((s)(i)(i)))((s)((s)((k)(s))(k))((k)((s)(i)(i))))

factorial = lambda f: lambda n: (1 if n<2 else n*f(n-1))
    
'''
>>> (s)(plus)(succ)(10)
21

(s_)(plus)(succ)(10)

>>> i(4)
4
>>> i_(4)
4

>>> (s)(plus)(i)(10)
20
>>> (s_)(plus)(i_)(10)
20

y(factorial)(5)
120
'''

l1=y(factorial)(5)
#l2=y_(factorial)(5)

m1 = list(map (lambda x: x+1,[1,2,3]))
m2 = list(map (lambda x,y : x+y,[1,2,3],[20,20,30]))

f1 = list(filter(lambda x : x < 5,range(10)))

r1 = functools.reduce (lambda x,y : x+y,[1,2,3,4])

