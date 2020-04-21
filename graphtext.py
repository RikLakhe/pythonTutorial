import matplotlib.pyplot as plt
import numpy as np

## Create functions and set domain length
x = np.arange(1, 1.5, 0.001)
a = np.sqrt(x)
b = pow(10, x)
c = pow(x, 1.5)
d = pow(2, (np.sqrt(np.log2(x))))
e = pow(x, 5 / 3)
# y = 6 * np.log2(x) + 6 * x
# dy = (1 / 2) * pow(x, 2)

## Plot functions and a point where they intersect
# plt.plot(x, y)
# plt.plot(x, dy)
plt.plot(x, a)
# plt.plot(x, b)
plt.plot(x, c)
plt.plot(x, d)
plt.plot(x, e)
## Config the graph
plt.title('A Cool Graph')
plt.xlabel('n')
plt.ylabel('f(n)')
# plt.ylim([0, 4])
plt.grid(True)
plt.legend(["a","c","d","e"], loc='upper left')

## Show the graph
plt.show()
