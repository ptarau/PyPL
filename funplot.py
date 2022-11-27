import matplotlib.pyplot as plt
import numpy as np


def plot(f, a, b, n=100):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')

    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # ax.xaxis.set_ticks_position('bottom')
    # ax.yaxis.set_ticks_position('left')

    a = int(n * a)
    b = int(n * b)

    xs = [x / n for x in range(a, b)]
    print(xs)
    ys = [f(x) for x in xs]

    plt.plot(xs, ys, '-r', label=None)

    plt.show()


def f(x):
    return x * x - 8 * x + 1

plot(lambda x : 2*x+1, -10, 10)
#plot(f, -10, 10)
