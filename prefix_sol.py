def bin(n) :
  if n==0 : 
    yield 'o'
  else :
    for k in range(0,n) :    
      for l in bin(k) :
        for r in bin(n-1-k) :        
          yield (l,r)

# 1
def to_prefix(t) :
  stack=[]
  def to_pf(t) :
    if t=='o' :
      stack.append('o')
    else :
      left,right=t
      stack.append('*')
      to_pf(left)
      to_pf(right);
  to_pf(t)
  return stack

#2
def to_file(n) :
  with open('prefix.txt','w') as f :
    for t in bin(n) :
      for p in to_prefix(t) :
        print(p,end=' ',file=f)
      print('',file=f)

#3
def from_postfix(ws) :
  stack=[]
  for w in ws :
    if w=='o' :
      stack.append(w)
    else :
      assert w=='*'
      x=stack.pop()
      y=stack.pop()
      stack.append((x,y))
  return stack.pop()

def from_file() :
  with open('prefix.txt', 'r') as f:
    text=f.read()
    lines = text.split('\n')
    for l in lines :
      if not l : continue
      l=l[:-1]
      ws=l.split(' ')
      ws=reversed(ws)
      yield from_postfix(ws)

#4
def same_as_written(n) :
  to_file(n)
  gold=list(bin(n))
  silver=list(from_file())
  return gold==silver

def test(n) :
  to_file(n)
  for x in from_file(): print(x)

test(5)
print('SAME_AS_WRITTEN:',same_as_written(5))

