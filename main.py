import numpy as np
import time
import sys
from quicksort import quicksort
from heapsort import heapsort
from insertion_sort import insertionSort
from bubble_sort import bubbleSort
sys.setrecursionlimit(9999999)

print("####QUICKSORT####")
# quicksort - losowe
a = np.random.randint(0, 2900, 2900)
r = len(a)-1
start = time.time()
quicksort(a, 0, r)
end = time.time()
print(f'{end-start} -> losowy - quicksort ')

# # quicksort - posortowane

# start = time.time()
# quicksort(a, 0, r)
# end = time.time()
# print(f'{end-start} -> posortowany - quicksort ')

# quickosrt - odwrotnie posortowane
a = a[::-1]
start = time.time()
quicksort(a, 0, r)
end = time.time()
print(f'{end-start} -> odwrotny - quicksort')

print("####HEAPSORT####")
# heapsort - losowe
a = np.random.randint(0, 100000, 100000)
start = time.time()
heapsort(a)
end = time.time()
print(f'{end-start} -> losowy - heapsort')

# heapsort - posortowane
start = time.time()
heapsort(a)
end = time.time()
print(f'{end-start} -> posortowany - heapsort')


# heapsort - odwrotnie posortowane
a = a[::-1]
start = time.time()
heapsort(a)
end = time.time()
print(f'{end-start} -> odwrotny - heapsort')


# insertion - losowe
a = np.random.randint(0, 10000, 10000)
start = time.time()
insertionSort(a)
end = time.time()
print(f'{end-start} -> losowy - insertion_sort')

# insertion - posortowane
start = time.time()
insertionSort(a)
end = time.time()
print(f'{end-start} -> posortowany - insertion_sort')

# Insertion_sort - odwrotnie
a = a[::-1]
start = time.time()
insertionSort(a)
end = time.time()
print(f'{end-start} -> odwrotny - insertion_sort')


# bubble_sort - losowe
a = np.random.randint(0, 10000, 10000)
start = time.time()
bubbleSort(a)
end = time.time()
print(f'{end-start} -> losowy - bubble_sort')

# bubble_sort - posortowane
start = time.time()
bubbleSort(a)
end = time.time()
print(f'{end-start} -> posortowany - bubble_sort')

# bubble_sort - odwrotnie
a = a[::-1]
start = time.time()
bubbleSort(a)
end = time.time()
print(f'{end-start} -> odwrotny - bubble_sort')
