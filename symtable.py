class SymTab():
    def __init__(self):
        """
        create map from symbols to numbers and back
        """
        self.ks = dict()
        self.vs = []

    def add(self, k):
        if k in self.ks:
            return self.ks[k]
        v = len(self.vs)
        self.ks[k] = v
        self.vs.append(k)

    def __repr__(self):
        return self.ks.__repr__()

    def __call__(self, x):
        if isinstance(x, str):
            return self.ks[x]
        return self.vs[x]


def test_symtable():
    s = SymTab()
    s.add('hello')
    s.add('bye')
    s.add('ok')
    print('SymTable:', s)
    print('bye:', s('bye'))
    print('ok:', s('ok'))
    print(0, ':', s(0))


if __name__ == '__main__':
    test_symtable()
