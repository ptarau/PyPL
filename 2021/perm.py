# insert an element in all possible places
def ins(x,xs) :
  for i  in range(len(xs)) :
    yield xs[:i]+[x]+xs[i:]
  yield xs + [x]

# insert first in each permutation of the rest of a list
def perm(xs) :
  if not xs : yield []
  else :
    for ps in perm(xs[1:]) :
      for rs in ins(xs[0],ps) :
        yield rs


# alternative, with immutable

import immutables as im

def selectFirst(Xs):
  if not Xs:
    return None
  else:
    X, Ys = Xs
    yield (X, Ys)
    for (Z, Zs) in selectFirst(Ys):
      yield (Z, (X, Zs))


def perm1(Xs):
  if not Xs:
    yield None
  else:
    for (X, Ys) in selectFirst(Xs):
      for Zs in perm1(Ys):
        yield (X, Zs)


def permute(Ls):
  Is = im.fromList(Ls)
  for Ps in perm1(Is):
    yield im.toList(Ps)


# tests

t1 = list(ins('*',[1,2,3]))

def t2() :
  for p in perm([1,2,3]) :
    print(p)

t5 = list(selectFirst((0,(1,(2,(3,None))))))

t6 = list(perm1((0,(1,(2,(3,(4,None)))))))

t7 = im.fromList([0,1,2,3,4])

t8 = im.toList(t7)

t5 = list(permute([1,2,3,4]))

def t6() :
 for P in  permute([1,2,3,4]) :
   print(P)

if __name__ == "__main__" :
  t2()
   

