def nats():
    i = 0
    while True:
        yield i
        i += 1

def take(n, g):
    i = 0
    for x in nats():
        if i >= n: break
        yield x
        i += 1


def odds():
    for x in nats() :
        if x % 2 == 1:
            yield x

def evens():
    for x in nats() :
        if x % 2 == 0:
            yield x


def pp(g,n=5) :
    for x in take(n,g):
        print(x)


xs=[x  for x in take(10,nats()) if x % 2==0]

ys={x  for x in take(10,nats()) if x % 2==0}


def qsort(xs) :
    if xs==[] : return xs
    pivot=xs[0]
    little_ones=[x for x in xs[1:] if x <= pivot]
    big_ones = [x for x in xs[1:] if x > pivot]
    return qsort(little_ones) + [pivot] + qsort(big_ones)
