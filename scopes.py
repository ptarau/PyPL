# scopes

ctr=0

def fun() :
  global ctr
  temp=10
  def inner() :
    nonlocal temp
    print(temp)
    temp=temp*temp

  ctr+=1
  inner()
  print(temp)

fun()
print(ctr)
