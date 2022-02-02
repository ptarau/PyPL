# insert an element in all possible places
def ins(x,xs) :
  for i  in range(len(xs)) :
    yield xs[:i]+[x]+xs[i:]
  yield xs + [x]

# insert first in each permutation of the rest of a list
def perm(xs) :
  if not xs : yield xs
  else :
    for ps in perm(xs[1:]) :
      #for rs in ins(xs[0],ps) :
        #yield rs
      yield from ins(xs[0],ps)



# tests

t1 = list(ins('*',[1,2,3]))

def t2() :
  for p in perm([1,2,3]) :
    print(p)


if __name__ == "__main__" :
  t2()
   

