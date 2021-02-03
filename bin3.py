# binary tree of size n
def bin3(n) :
  if n==0 : 
    yield 'red'
    yield 'green'
    yield 'blue'
  else :
    for k in range(0,n) :    
      for l in bin3(k) :
        for r in bin3(n-1-k) :        
          yield (l,r)
'''
>>> for t in bin3(2) : print(t)

('red', ('red', 'red'))
('red', ('red', 'gree'))
('red', ('red', 'blue'))
('red', ('gree', 'red'))
('red', ('gree', 'gree'))
('red', ('gree', 'blue'))
('red', ('blue', 'red'))
('red', ('blue', 'gree'))
('red', ('blue', 'blue'))
('gree', ('red', 'red'))
('gree', ('red', 'gree'))
('gree', ('red', 'blue'))
('gree', ('gree', 'red'))
('gree', ('gree', 'gree'))
('gree', ('gree', 'blue'))
('gree', ('blue', 'red'))
('gree', ('blue', 'gree'))
('gree', ('blue', 'blue'))
('blue', ('red', 'red'))
('blue', ('red', 'gree'))
('blue', ('red', 'blue'))
('blue', ('gree', 'red'))
('blue', ('gree', 'gree'))
('blue', ('gree', 'blue'))
('blue', ('blue', 'red'))
('blue', ('blue', 'gree'))
('blue', ('blue', 'blue'))
(('red', 'red'), 'red')
(('red', 'red'), 'gree')
(('red', 'red'), 'blue')
(('red', 'gree'), 'red')
(('red', 'gree'), 'gree')
(('red', 'gree'), 'blue')
(('red', 'blue'), 'red')
(('red', 'blue'), 'gree')
(('red', 'blue'), 'blue')
(('gree', 'red'), 'red')
(('gree', 'red'), 'gree')
(('gree', 'red'), 'blue')
(('gree', 'gree'), 'red')
(('gree', 'gree'), 'gree')
(('gree', 'gree'), 'blue')
(('gree', 'blue'), 'red')
(('gree', 'blue'), 'gree')
(('gree', 'blue'), 'blue')
(('blue', 'red'), 'red')
(('blue', 'red'), 'gree')
(('blue', 'red'), 'blue')
(('blue', 'gree'), 'red')
(('blue', 'gree'), 'gree')
(('blue', 'gree'), 'blue')
(('blue', 'blue'), 'red')
(('blue', 'blue'), 'gree')
(('blue', 'blue'), 'blue')
>>> 

'''


