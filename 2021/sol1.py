# ternary=binary-unary tree of size n
# cost of ternary nodes=3, size of binary nodes=2, size of unary nods=1
def mot3 (n) :
  if n==0 :
    yield []
  else :
    for m in mot3(n-1) :
      yield [m]
    for k in range(0,n-1) :
      for l in mot3(k) :
        for r in mot3(n-2-k) :
          yield (l,r)
    for k in range (0,n-3) :
      for a,b,c in split(k) :
        for l in mot3(a) :
          for m in mot3(b) :
            for r in mot3(c) :
              yield (l,m,r)

def split(k) :
  for a in range(k) :
    for b in range(k) :
      for c in range(k) :
        if a+b+c == k :
          yield a,b,c

def test1() :
  for x in split(4) : 
    print(x)
  print('')

  for t in mot3(5) :
    print(t)
  print()

test1()

# rose tree (multi-way tree) of size n
def rose(n):
  if n == 0:
    yield []
  else:
    for k in range(0, n):
      for l in rose(k):
        for r in rose(n - 1 - k):
          yield [l] + r
          
# rose tree of size n with branches of size at most 3
# with cost of each internal node 1
def rose3(n):
  if n == 0:
    yield []
  else:
    for k in range(0, n):
      for l in rose3(k):
        for r in rose3(n - 1 - k):
          if len(r)<=2:
            yield [l] + r

def test2() :
  for t in rose3(5) :
    print(t) 
    
test2()
