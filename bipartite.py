class BipartiteGraph:
    def __init__(self):
        self.left = dict()
        self.right = dict()

    def add(self, l, r):
        if l not in self.left:
            self.left[l] = set()
        if r not in self.right:
            self.right[r] = set()
        self.left[l].add(r)
        self.right[r].add(l)

    def __repr__(self):
        return str(self.left) + ', ' + str(self.right)


b=BipartiteGraph()

b.add('Joe','milk')
b.add('Joe','eggs')
b.add('Joe','wine')

b.add('Mary','milk')
b.add('Mary','chicken')
b.add('Mary','brocli')
b.add('Bill','wine')

print(b)
