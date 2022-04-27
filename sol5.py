g = {
    0: [1, 2, 3],
    1: [0, 3],
    2: [1],
    4: [],
    5: [2, 3]
}


def has_cycle(g):
    seen = set()

    def walk(start):
        print(start)
        if start not in g:
            return
        ns = g[start]
        for n in ns:
            if n in seen:
                return True
            seen.add(n)
            return walk(n)
        return False
    return walk(0)


def edges_of(g):
    es = [(x, y) for x, ys in g.items() for y in ys]
    return es


def nodes_of(g):
    ns = [x for x in g]
    ms = [y for _, ys in g.items() for y in ys]
    return sorted(set(ns + ms))


def to_matrix(g):
    ns = nodes_of(g)
    dim = len(ns)
    mat = [[0] * dim for _ in range(dim)]
    for (i, j) in edges_of(g):
        mat[i][j] = 1
    return mat


def show(mat):
    for row in mat:
        print(row)


print(g)

print(has_cycle(g))

print(to_matrix(g))

print(nodes_of(g))

show(to_matrix(g))
