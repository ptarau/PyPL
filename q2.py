

def q2(es) :
  # find all nodes
  ns = sorted({x for e in es for x in e})

  # find set of incoming edges to n
  def incomings_of(n) :
    return {m for m in ns if (m, n) in es}

  # collect them, for each node
  ins = {(n,len(incomings_of(n))) for n in ns }

  # sort them
  ins = sorted(ins,reverse=True,key=lambda x:x[1])

  # return their nodes
  return [n for (n,_) in ins]


def test():
  es={(1,2),(1,3),(1,6),(2,4),(5,6),(6,2),(3,8),(2,9),(2,10),
      (3,6),(7,6),(6,6),(5,5),(4,9),(1,10),(10,7),(8,10),(10,1),(4,6),(10,3)}

  print(q2(es))

test()
