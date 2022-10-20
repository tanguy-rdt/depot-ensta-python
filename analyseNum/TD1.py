import sys

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plot


def f1(x):
    return ((x**3)-x)

def f2(x):
    return (np.sin(x))

def f3(x):
    return 2*x*(np.exp(-(x)**2))

def f4(x):
    return 4*(x) + 2

def F1(x):
    return ((x**4)/4) - ((x**2)/2)

def F2(x):
    return -(np.cos(x))

def F3(x):
    return -(np.exp((-x)**2))

def F4(x):
    return 2*(x)**2 + 2*x

def rectangle_gauche(a, b, n, f):
    pas = (b - a) / n
    return pas * np.sum(f(np.arange(a, b - pas / 2, pas)))

def main():
    fct = input("fonction (f1, f2...): ")
    a = int(input("borne a: "))
    b = int(input("borne b: "))

    if fct == "f1":
        f = f1
        F = F1
    elif fct == "f2":
        f = f2
        F = F2
    elif fct == "f3":
        f = f3
        F = F2
    elif fct == "f4":
        f = f4
        F = F4

    n_test = [10, 100, 1000, 10000]
    err = []

    exacte = F(b)-F(a)

    for n in n_test:
        estimer = rectangle_gauche(a, b, n, f)
        err.append(np.abs(exacte-estimer))

    plt.loglog(n_test, err)
    plt.ylabel("err")
    plt.xlabel("n_test")
    plt.show()

    print("estimer: %s" % estimer)
    print("exact %s" % exacte)
    print("erreur: %s" % np.abs(exacte - estimer))
    print("erreur list: %s" % err)




if __name__ == '__main__':
    main()
