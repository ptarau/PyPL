import immutables as im

def selectFirst(Xs) :
  if not Xs : return None
  else :
    X,Ys = Xs
    yield (X,Ys)
    for (Z,Zs) in selectFirst(Ys) :
      yield (Z,(X,Zs))

def perm(Xs) :
  if not Xs : yield None
  else :
    for (X,Ys) in selectFirst(Xs) :
      for Zs in perm(Ys) :
        yield (X,Zs)


def permute(Ls) :
  Is = im.fromList(Ls)  
  for Ps in perm(Is) :
    yield im.toList(Ps)
  
  
t1 = list(selectFirst((0,(1,(2,(3,None))))))

t2 = list(perm((0,(1,(2,(3,(4,None)))))))

t3 = im.fromList([0,1,2,3,4])

t4 = im.toList(t3)

t5 = list(permute([1,2,3,4]))

def go() :
 for P in  permute([1,2,3,4]) :
   print(P)
   

