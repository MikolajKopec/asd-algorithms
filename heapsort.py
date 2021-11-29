def max_heapify(A, k, s):
    l = left(k)
    r = right(k)
    if l < s and A[l] > A[k]:
        largest = l
    else:
        largest = k
    if r < s and A[r] > A[largest]:
        largest = r
    if largest != k:
        A[k], A[largest] = A[largest], A[k]
        max_heapify(A, largest, s)


def left(k):
    return 2 * k + 1


def right(k):
    return 2 * k + 2


def build_max_heap(A, s):
    n = int((s//2)-1)
    for k in range(n, -1, -1):
        max_heapify(A, k, s)


def heapsort(a):
    s = len(a)
    build_max_heap(a, s)
    for i in range(len(a)-1, 0, -1):
        s = s-1
        h = a[0]
        a[0] = a[i]
        a[i] = h
        max_heapify(a, 0, s)
