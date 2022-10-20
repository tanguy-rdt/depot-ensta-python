import matplotlib.pyplot as plt
import numpy as np


def calc(t0, tmax, h, y0, f):
    t = t0
    y_euler = y0


    save_t = []
    save_y_euler = []

    save_t.append(t0)
    save_y_euler.append(y_euler)

    while t < tmax:
        y_euler = y_euler + h * f(t, y_euler)
        t += h
        save_y_euler.append(y_euler)
        save_t.append(t)

    return save_t, save_y_euler


def f(t, y):
    a = -1
    return -a * y


def main():
    save_t, save_y_euler = calc(0, 10, 0.01, 1, f)

    a = -1
    save_y_exact = np.exp(-a*save_t)


    plt.plot(save_t, save_y_euler)
    plt.plot(save_t, save_y_exact)

    plt.show()


if __name__ == '__main__':
    main()
