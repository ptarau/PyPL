def subset(Xs) :
  if  Xs == [] : yield Xs # is empty
  else :
    X = Xs[0] # head
    Ys = Xs[1:] # tail
    for Zs in subset(Ys) :
      yield Zs # inherit from the subsets of tail
      yield [X] + Zs # extend the subsets of tail

    
def test() :
  for t in subset( [0,1,2,3] ) : print(t)


"""

 subsets equal in size to their complements

 U={1,2,3,4}

{1,3} and {2,4}
{1,4} and {2,3}
{1,2} and {3,4}
{2,4} and {1,2}
"""
