def producer(k):
    if k>0:
        r=(yield from producer(k-1))
    else:
        r=(yield k)
    #print(r)
    return r


def loop(k):
    # while True:
    p=producer(k)
    print(p)
    for x in p:
        print(x)


loop(3)
