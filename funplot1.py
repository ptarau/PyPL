import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

x = np.linspace(-5,5,100)


plt.plot(x, 2*x+1, '-r', label='y=2x+1')
plt.plot(x, 2*x-1,'-.g', label='y=2x-1')
plt.plot(x, 2*x+3,':b', label='y=2x+3')
plt.plot(x, 2*x-3,'--m', label='y=2x-3')

plt.legend(loc='upper left')
plt.show()
