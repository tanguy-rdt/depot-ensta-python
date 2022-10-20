# -*- coding: utf-8 -*-
import numpy as np
import time


def average(a):
    """
    Compute the average value of ``a``

    Parameters
    ----------
    a : ndarray
        Input array.

    Returns
    -------
    avg : int
        The average value of ``a``
    """

    average = 0
    for i in range(a.shape[0]):
        average += a[i] #somme de tous les coefs du tab
    return average/a.shape[0] #return une moyenne


if __name__ == "__main__":
    rand_array_1 = np.random.randint(0, 10000, 10000) #start, end N
    t0 = time.perf_counter_ns() # initialisation du temps
    average_value = average(rand_array_1) # calcul de la moyenne avec notre fct (donc avec un for)
    print(time.perf_counter_ns() - t0)  # affiche le temps qui s'est écoulé depuis t0

    t0 = time.perf_counter_ns() # initialisation du temps
    average_value = np.mean(rand_array_1) # calcul de la moyenne avec la fonction de numpy
    print(time.perf_counter_ns() - t0)


#   Le programme affiche le temps mis pour faire la moyenne en utilisant
#   la fonction de numpy et en ustilisant un for. La fonction de numpy
#   est plus rapide comme elle utilise moins de mém

