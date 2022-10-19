import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def f(x, y):
    return x ** 2 - y ** 2

def surface():
    x = y = np.arange(-3.0, 3.0, 0.05)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z)

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    plt.show()

def field():
    x = y = np.arange(-2.0, 2.0, 0.3)

    X, Y = np.meshgrid(x, y)

    u = f(X, Y)
    v = np.ones(u.shape)

    plt.quiver(X, Y, u, v)
    plt.show()

if __name__ == "__main__":
    surface()
    field()