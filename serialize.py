import networkx as nx
import matplotlib.pyplot as plt
import pickle
import json

def show_graph(g) :
  nx.draw(g,with_labels=True, font_weight='bold')
  plt.show()


# npickeling
def to_file(obj,fname) :
  with open(fname, "wb") as outf:
    pickle.dump(obj,outf)

def from_file(fname) :
  with open(fname, "rb") as inf:
    return pickle.load(inf)

def test() :
  D = nx.DiGraph()
  D.add_edge("a", "b")
  D.add_edge("b", "c")
  D.add_edge("a", "c")

  show_graph(D)
  fname='graph.bin'
  to_file(D,fname)
  PickledD=from_file(fname)
  show_graph(PickledD)

#test1()

# json serialization
def to_json(g,fname) :
  es=list(g.edges())
  with open(fname, "w") as outf:
    json.dump(es,outf)

def from_json(fname) :
  with open(fname, "r") as inf:
    es = json.load(inf)
    D=nx.DiGraph()
    D.add_edges_from(es)
    return D

def test2() :
  D = nx.DiGraph()
  D.add_edge("a", "b")
  D.add_edge("b", "c")
  D.add_edge("a", "c")

  show_graph(D)
  fname='graph.json'
  to_json(D,fname)
  print('back from json')
  PickledD=from_json(fname)
  show_graph(PickledD)

test2()
