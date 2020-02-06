def file2string(fname) :
  with open(fname,'r') as f:
    return f.read()

def string2file(string,fname) :
  with open(fname,'w') as g:
    g.write(string)

def file2lines(fname) :
  with open(fname,'r') as f:
    return [l.replace('\n','') for l in f.readlines()]

def go1():
  s=file2string('examples/temp.txt')
  string2file(s,'examples/temp1.txt')
  print(s)

import nltk

def go() :
  ls=file2lines('examples/temp.txt')
  print(ls)

go()
