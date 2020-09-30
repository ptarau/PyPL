p=0
q=1
r=1
s=0

def f(p,q,r,s) :
  return (p and q) or (q and s) or (not p)

def g(p,q,r,s) :
  return ((p or not q) or (not q and not s) and (not p)) and (p and not p)


def t1() :
  print(f(p,q,r,s))

def sat() :
  for p in (0,1) :
    for q in (0, 1):
      for r in (0, 1):
        for s in (0, 1):
          if f(p,q,r,s) :
            yield (p,q,r,s)

def unsat() :
  for p in (0,1) :
    for q in (0, 1):
      for r in (0, 1):
        for s in (0, 1):
          if not f(p,q,r,s) :
            yield (p,q,r,s)

def truth_table4(fun) :
  for p in (0, 1):
    for q in (0, 1):
      for r in (0, 1):
        for s in (0, 1):
          if fun(p, q, r, s):
            yield (p, q, r, s)

def t2() :
  for t in sat() :
    print(t)


def t3():
  return len(list(sat()))

def t4():
  return len(list(unsat()))

def t5() :
  for t in unsat() :
    print(t)

def t6() :
  for t in truth_table4(g) : print(t)

