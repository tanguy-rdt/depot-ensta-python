import time

import numpy as np
import matplotlib.pyplot as plt


def init_list(n=10, m=10, seed=4242):
    np.random.seed(seed)
    return np.random.randint(0, m, n)


def is_sorted(tab):
    for i in range(len(tab) - 1):
        if tab[i] > tab[i + 1]:
            return False

    return True


def find_seed_sort(n, m):
    for s in range(100000):
        tab = init_list(n, m, seed=s)
        if is_sorted(tab):
            return s


def selection_sort(array_to_sort_orig):
    # utile seulement dans le cadre du TP pour éviter de trier le tableau en paramètre
    array_to_sort = array_to_sort_orig.copy()
    t_start = time.time()
    last = len(array_to_sort)
    while last:  # tant que last != 0
        max_idx = 0
        for idx in range(last):
            if array_to_sort[idx] > array_to_sort[max_idx]:
                max_idx = idx
        array_to_sort[last - 1], array_to_sort[max_idx] = array_to_sort[max_idx], array_to_sort[last - 1]
        last -= 1
    delta_t = time.time() - t_start

    return delta_t, array_to_sort

"""On prend un élément, si l'élement suivant (j) est plus petit que le précédent (j-1). (j) devient (j-1) et etc
jusqu'à arriver à la fin du tableau"""
def tri_insertion(tab):
    start_time = time.time()

    for i in range(1, len(tab)):
        x = tab[i]

        j = i
        while j >= 1 and tab[j - 1] > x:
            tab[j] = tab[j - 1]
            j = j - 1

        tab[j] = x

    end_time = time.time()
    process_time = end_time - start_time

    return tab, process_time


def tri_shell(tab):
    start_time = time.time()

    def get_gaps(tableau):
        gap = 0
        gaps = []
        while gap < len(tableau):
            gap = 3 * gap + 1
            gaps.append(gap)

        return np.flip(gaps)

    def tri_insert(tab, gap=1):
        for i in range(gap, len(tab)):
            x = tab[i]

            j = i
            while j >= gap and tab[j - gap] > x:
                tab[j] = tab[j - gap]
                j = j - gap

            tab[j] = x

        return tab

    gaps = get_gaps(tab)

    for gap in gaps:
        tab_sort = tri_insert(tab, gap)

    end_time = time.time()
    process_time = end_time - start_time

    return tab_sort, process_time


def partition_hoore(arr, low, high):
    pivot = arr[0]
    low = low - 1
    high = high + 1
    while True:
        low = low + 1
        high = high - 1

        while arr[low] < pivot:
            low = low + 1

        while arr[high] > pivot:
            high = high - 1

        if low > high:
            return high

        a_low = arr[low]
        a_high = arr[high]

        arr[low] = a_high
        arr[high] = a_low


def quick_sort(arr, low, high):
    if low < high:
        index = partition_hoore(arr, low, high)
        quick_sort(arr, low, index)
        quick_sort(arr, index + 1, high)


# tab = init_list()
# print("list:", tab)
# print("sum:", np.sum(tab))
# print("tab is sorted:", is_sorted(tab))
# print("tab is sorted with:", find_seed_sort(10, 10)) #99077

""" Tri par sélection """
# tab = np.array([4, 3, 2, 1])
# array_sorted_time, array_sorted = selection_sort(tab)
# print("Take the time %s s, for sort the table tab %s to %s" %(array_sorted_time, tab , array_sorted))

""" Tri par insertion """
# tab = init_list(n=10000, m=20000)
# print("tab avant tri par insertion: ", tab)
# print("tab après tri par insertion: ", tri_insertion(tab))
# print("val de l'index 200: ", tab[200])
# print("val de l'index 9090: ", tab[9090])

""" Tri shell """
tab = init_list(n=100000, m=499999)
print("tab avant tri shell: ", tab)
tab_sorted, process_time = tri_shell(tab)
print("tab après tri shell: ", tab_sorted)
print("val de l'index 100: ", tab[100])
print("val de l'index 80808: ", tab[80808])
print("Temps d'execution", process_time)

""" Partition de Hoore """
# A = [12, 25, 42, 3, 4, 13]
# index = partition_hoore(A, 0, len(A)-1)
# print("A: ", A)
# print("Index de sep: ", index)
