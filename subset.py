import immutables as im

def subset(Xs) :
  if not Xs : yield Xs # ir empty
  else :
    X = Xs[0] # head
    Ys = Xs[1:] # tail
    for Zs in subset(Ys) :
      yield Zs # inherit from the subsets of tail
      yield [X] + Zs # extend the subsets of tail

def subset1(Xs) :
  if not Xs : yield None
  else :
    X,Ys = Xs
    for Zs in subset1(Ys) :
      yield Zs
      yield (X,Zs)

t1 = list(subset1((1,(2,(3,(4,None))))))

def t2() : 
  for X in subset1(im.fromList([1,2,3,4])) :
    print(im.toList(X))
    
def t3() : 
  for t in subset( [0,1,2,3] ) : print(t)
