import networkx as nx
import numpy as np

import matplotlib.pyplot as plt

def show_graph(g) :
  nx.draw(g,with_labels=True, font_weight='bold')
  plt.show()

U=nx.Graph()
U.add_edge("a","b")
U.add_edge("b","c")
U.add_edge("a","c")

D=nx.DiGraph()
D.add_edge("a","b")
D.add_edge("b","c")
D.add_edge("a","c")


class MyGraph:
  def __init__(self,arg,directed=False):
    if directed : self.g=nx.DiGraph(arg)
    else: self.g = nx.Graph(arg)


  def show(self): show_graph(self.g)


G=MyGraph([(1,2),(2,3),(3,1)],directed=False)
G.show()

#show(D)

def plot1() :
  G = nx.petersen_graph()
  plt.subplot(121)
  nx.draw(G, with_labels=True, font_weight='bold')
  plt.subplot(122)
  nx.draw_shell(G,
                nlist=[range(5, 10),
                       range(5)],
                with_labels=True,
                font_weight='bold')
  plt.show()


def plot2() :
  G = nx.petersen_graph()
  nx.draw(G, with_labels=True, font_weight='bold')
  plt.show()


#plot1()
