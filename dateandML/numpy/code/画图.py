import matplotlib.pyplot as plt
import numpy as np
# fig = plt.figure()
# ax1 = fig.add_subplot(211)
# t = np.arange(0.0, 1.0, 0.01)
#
# s = np.sin(2 * np.pi * t)
# line, = ax1.plot(t, s, color='green', lw=5)
# # fig2 = plt.figure()
# # ax2 = fig2.add_axes([0.15, 0.1, 0.7, 0.3])
# plt.show()

# np.random.seed(100)
fig = plt.figure()
ax1 = fig.add_subplot(211)
n, bins, patches = ax1.hist(np.random.randn(10000), 100, facecolor='yellow', edgecolor='green')
plt.show()