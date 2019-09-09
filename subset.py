import immutables as im

def subset(Xs) : 
  if not Xs : yield None
  else :
    X,Ys = Xs
    for Zs in subset(Ys) :
      yield Zs
      yield (X,Zs)
     
def subset1(Xs) : 
  if not Xs : yield Xs
  else :
    X = Xs[0]
    Ys = Xs[1:]
    for Zs in subset1(Ys) :
      yield Zs
      yield (X,) + Zs
     
t1 = list(subset((1,(2,(3,(4,None))))))   

def t2() : 
  for X in subset(im.fromList([1,2,3,4])) : 
    print(im.toList(X))
    
def t3() : 
  for t in subset1( (0,1,2,3) ) : print(t)
