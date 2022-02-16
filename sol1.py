def ksubset(k, xs):
    if k == 0:
        yield []
    elif xs == []:
        return []
    else:
        x = xs[0]
        ys = xs[1:]
        for zs in ksubset(k - 1, ys):
            yield [x] + zs
        for us in ksubset(k, ys):
            yield us


def subsets_of(xs):
    for k in range(len(xs)):
        yield from ksubset(k, xs)
    yield xs


def test1(n):
    xs = list(range(n))
    for ys in ksubset(n // 2, xs):
        print(n // 2, ys)


def test(n):
    xs = list(range(n))
    for xs in subsets_of(xs):
        print(xs)


if __name__ == "__main__":
    test(5)
