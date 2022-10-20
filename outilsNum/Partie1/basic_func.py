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
        average += a[i]
    return average/a.shape[0]


if __name__ == "__main__":
    rand_array_1 = np.random.randint(0, 10000, 10000)

    t0 = time.perf_counter_ns()
    average_value = average(rand_array_1)
    print(time.perf_counter_ns() - t0)

    t0 = time.perf_counter_ns()
    average_value = np.mean(rand_array_1)
    print(time.perf_counter_ns() - t0)
