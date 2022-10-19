import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import derivative

def f(x):
	return np.sin(x)

x = np.linspace(-np.pi, np.pi, 201)

f_diff = derivative(f, x, dx=1e-10)

plt.xlabel('x')
plt.ylabel('y')

plt.plot(x, f(x), label="f(x)")
plt.plot(x, f_diff, label="f'(x)")

plt.legend(loc="upper left")
plt.axis('tight')
plt.grid(True)

plt.show()

