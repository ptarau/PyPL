import networkx as nx

d = {
    0: [1, 2, 3],
    1: [0, 3],
    2: [1],
    4: [],
    5: [2, 3]
}

g = nx.DiGraph(d)

def has_cycle(g):
    try:
       nx.find_cycle(g)
       return True
    except nx.exception.NetworkXNoCycle:
       return False

def to_matrix(g):
    return nx.to_numpy_array(g,dtype=int)


print(g)

print(has_cycle(g))

print(to_matrix(g))
