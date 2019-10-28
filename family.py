class person :
  def __init__(self,name,gender,father,mother):
    self.name = name
    self.gender = gender
    self.father = father
    self.mother = mother

adam=person('Adam','male',None,None)
eve=person('Eve','female',None,None)

abel=person('Abel','male',adam,eve)

def t1() :
  print(abel.father.name)
  print(abel.mother.name)

t1()
