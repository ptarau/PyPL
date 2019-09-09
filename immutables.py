def fromList(Ls) :
  Xs = None
  Rs = Ls.copy()
  while Rs :
    X = Rs.pop()
    Xs = X,Xs
  return Xs
  
def toList(Is) : 
  return list(inImmutable(Is))
  
def inImmutable(Is) :
  if not Is : return None
  else :
    I,Js = Is
    yield I
    for J in inImmutable(Js) : yield J 
    
