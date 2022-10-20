

def build_heap(arr):
    n = len(arr)

    for k in range (n//2, -1, -1):
        heapify(arr, n, k)

    return arr


def heapify(arr, n, heap_start):
    idx_left = 2 * heap_start + 1
    idx_right = 2 * heap_start + 2
    idx_largest = heap_start

    if (idx_left < n) and (arr[idx_left] > arr[idx_largest]):
        idx_largest = idx_left
    if (idx_right < n) and (arr[idx_right] > arr[idx_largest]):
        idx_largest = idx_right
    if idx_largest is not heap_start:
        val_heap_start = arr[heap_start]
        arr[heap_start] = arr[idx_largest]
        arr[idx_largest] = val_heap_start

        heapify(arr, n, idx_largest)

def heap_sort(arr):
    n = len(arr)
    build_heap(arr)

    for k in range (n):
        val_max = arr[0]
        arr[0] = arr[n-k] # ne marche pas comme k vaut 0 mais on à le max en position 0 il suffit de le mettre en
        #en dernier position qui n'est pas déjà trié, et on obtiendra une liste trié avec le max en n position
        arr[n-k] = val_max

        heapify(arr, n-k, 0)

    return arr





if __name__ == '__main__':
    arr = [5, 4, 8, 25, 12, 42, 3, 42, 58]
    arr_sort = build_heap(arr)

    print("Question 2, on à %s" %(arr_sort))
    print("Donc oui le résultat est cohérent avec celui attendu, un tas", end="\n")
    # résultat: [5, 4, 8, 25, 12, 42, 3, 42, 58] --> [58, 42, 42, 25, 12, 8, 3, 4, 5]

    arr = [8, 56, 2, 5, 23, 216, 39, -5, 3, 8]
    arr_sort = heap_sort(arr)
    print("Question 3, on à %s" %(arr_sort))
    print("Donc oui le résultat est cohérent avec celui attendu, une liste trié", end="\n")

