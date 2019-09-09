# binary and binary-unary (Mozkin) tree generators

# binary tree of size n
def bin(n) :
  if n==0 : 
    yield n
  else :
    for k in range(0,n) :    
      for l in bin(k) :
        for r in bin(n-1-k) :        
          yield (l,r)

# Motzkin tree of size n
def mot (n) :
  if n==0 : 
    yield n
  else :
    for m in mot(n-1) :
      yield [m]
    for k in range(0,n-1) :    
      for l in mot(k) :
        for r in mot(n-2-k) :        
          yield (l,r)

def countFor(f,n) :
  for i in range(n) :
    count = 0
    for t in f(i) : 
      count+=1
    yield count

def countsFor(mes,f,n) :
  print(mes)
  print([c for c in countFor(f,n)])
  print("")

def showFor(mes,f,n) :
  print(mes)
  for t in f(n) :
    print(t)
  print("")
 
showFor('Binary trees',bin,3)
showFor('Motzkin trees',mot,4)

countsFor('Binary trees',bin,12)
countsFor('Motzkin trees',mot,12)

print("done")

def test() :
  for n in range(6) :
    print(n,list(mot(n)))          
