'''
algorithms.py
'''
def bubble_sort(array):
    n = len(array)

    for i in range(n):
        for j in range(0, n-i-1):
            yield 0, j, j+1, array
            if array[j] > array[j+1]:
                yield 1, j, j+1, array
                array[j], array[j+1] = array[j+1], array[j]
                yield 2, j, j+1, array
