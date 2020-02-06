import nltk
import json

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

def go2() :
  ls=file2lines('examples/temp.txt')
  print(ls)

def go3():
  s = file2string('examples/temp.txt')
  toks=nltk.word_tokenize(s)
  for t in toks :
    print(t)

def go():
  s = file2string('examples/temp.txt')
  toks=list(nltk.word_tokenize(s))
  d={'examples/temp.txt':toks,'date':"6 feb 20"}
  with open('examples/temp.json','w') as g:
    json.dump(d,g)
  with open('examples/temp.json','r') as f:
    d1=json.load(f)
    print(d1)

go()
