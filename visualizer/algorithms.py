'''
algorithms.py
algorithm information and help received from website: geeksforgeeks.org
'''
'''Bubble Sort'''
def bubble_sort(array):
    n = len(array)
    for pass_num in range(n-1, 0, -1):
        for j in range(pass_num):
            yield 'compare', array, j, j+1, None
            if array[j] > array[j+1]:
                yield 'swapping', array, j, j+1, None
                array[j], array[j+1] = array[j+1], array[j]
                yield 'draw all', array, j, j+1, None

def fast_bubble_sort(array):
    n = len(array)
    for pass_num in range(n-1, 0, -1):
        swap = False
        for j in range(pass_num):
            yield 'compare', array, j, j+1, None
            if array[j] > array[j+1]:
                swap = True
                yield 'swapping', array, j, j+1, None
                array[j], array[j+1] = array[j+1], array[j]
                yield 'draw all', array, j, j+1, None


        if swap == False:
            raise StopIteration()

'''Selection Sort'''
def selection_sort(array):
    n = len(array)
    for fill_slot in range(n-1, 0, -1):
        position_max = 0
        yield 'compare', array, position_max, None, None
        for location in range(1, fill_slot + 1):
            yield 'compare', array, position_max, location, None
            if array[location] > array[position_max]:
                position_max = location
                yield 'compare', array, position_max, None, None

        yield 'compare', array, fill_slot, position_max, None
        (array[fill_slot],
        array[position_max]) = (array[position_max],
        array[fill_slot])
        yield 'swapping', array, fill_slot, position_max, None

'''Insertion Sort'''
def insertion_sort(array):
    n = len(array)
    yield 'swapping', array, None, None, 0
    for i in range(1, n, 1):
        item = array[i]
        j = i - 1
        yield 'compare', array, None, None, i
        while j >= 0 and item < array[j]:
            yield 'swapping', array, j+1, j, i
            array[j+1], array[j] = array[j], array[j+1]
            '''
            swap j+1, j for visualization purposes
            isntead of pulling the value out, moving all them up, then inserting
            '''
            yield 'swapping', array, j+1, j, i, None

            j-=1
        array[j+1] = item

        yield 'draw all', array, None, None, None

'''Shell Sort'''
def shell_sort(array):
    n = len(array)

    gap = n // 2

    while gap > 0:
        yield 'draw all', array,  None, None, None
        for i in range(gap, n):
            temp = array[i]

            j = i
            while j >= gap and array[j-gap] > temp:
                yield 'compare', array,  j, j-gap, None
                array[j] = array[j-gap]
                yield 'swapping', array, j, j-gap, None
                j-= gap

            array[j] = temp
            yield 'draw all', array, i, None, None

        gap //= 2


'''Heap Sort'''
def heap_sort(array):
    n = len(array)
    '''BUILDINGMAXHEAP FUNCTION'''
    for i in range(n):
        '''if arr[i](child) > arr[x]parent:'''
        if array[i] > array[int((i - 1) / 2)]:
            j = i
            while array[j] > array[int((j - 1) / 2)]:
                yield 'compare', array, j, int((j-1)/2), None
                (array[j],
                 array[int((j - 1) / 2)]) = (array[int((j - 1) / 2)],
                                           array[j])
                yield 'swapping', array, int((j-1)/2), j, None
                j = int((j - 1) / 2)
                yield 'draw all', array, None, None, None

    '''HEAP SORT'''
    yield 'draw all', None, None, None
    for i in range(n - 1, 0, -1):
        yield 'compare', array, i, 0, None
        array[0], array[i] = array[i], array[0]
        yield 'swapping', array, i, 0, None

        j, index = 0, 0

        while True:
            index = 2 * j + 1

            if (index < (i - 1) and
                array[index] < array[index + 1]):
                index += 1

            if index < i and array[j] < array[index]:
                yield 'compare', array, index, j, None
                array[j], array[index] = array[index], array[j]
                yield 'draw all', array, index, j, None

            j = index
            if index >= i:
                break

'''Merge Sort, adjusted from code @'''
'''https://github.com/Orangefish/algo/blob/master/sorting_and_search/sort_merge.py'''
def merge_sort(array, l=0, u=None):
    """
    Merge sorting, mutable input.
    Input Sequence changed in place.

    Time: O(n * log n)
        log n -- levels
        n -- elements on each level must be merged

    Space (additional): O(1)
        input changed in place
    Returns None
    """
    u = len(array) if u is None else u
    if  u - l > 1:
        m = l + (u - l) // 2
        w = l + u - m

        yield from wsort(array, l, m, w)

        while w - l > 2:
            n = w
            w = l + (n - l + 1) // 2

            yield from wsort(array, w, n, l)
            yield from wmerge(array, l, l + n - w, n, u, w)
        n = w

        while n > l: # fallback to insert sort
            for m in range(n, u):
                if array[m-1] > array[m]:
                    yield 'compare', array, m-1, m, None
                    array[m-1], array[m] = array[m], array[m-1]
                    yield 'swapping', array, m-1, m, None
            n -= 1

def wmerge(array, i, m, j, n, w):
    """
    Merge subarrays [i, m) and [j, n) into work area w.
    All indexes point into array.
    The space after w must be enough to fit both subarrays.
    """
    while i < m and j < n:
        if array[i] < array[j]:
            yield 'compare', array, i, w, None
            array[i], array[w] = array[w], array[i]
            yield 'swapping', array, i, w, None
            i += 1
        else:
            yield 'compare', array, j, w, None
            array[j], array[w] = array[w], array[j]
            yield 'swapping', array, j, w, None
            j += 1
        w += 1
    while i < m:
        yield 'compare',array,  i, w, None
        array[i], array[w] = array[w], array[i]
        yield 'swapping', array, i, w, None
        i += 1
        w += 1
    while j < n:
        yield 'compare', array, j, w, None
        array[j], array[w] = array[w], array[j]
        yield 'swapping', array, j, w, None
        j += 1
        w += 1

def wsort(array, l, u, w):
    """
    Sort subarray [l, u) and put reuslt into work area w.
    All indexes point into array.
    """
    if  u - l > 1:
        m = l + (u - l) // 2
        yield from merge_sort(array, l, m)
        yield from merge_sort(array, m, u)
        yield from wmerge(array, l, m, m, u, w)
    else:
        while l < u:
            yield 'compare', array, l, w, None
            array[l], array[w] = array[w], array[l]
            yield 'swapping', array, l, w, None
            l +=1
            w +=1

'''Quick Sort - Lomuto-Partition'''
def quick_sort(array):
    n = len(array)
    yield from quick_sort_helper(array, 0, n-1)

def quick_sort_helper(array, low, high):
    if low < high:
        '''PARTITION FUNCTION START'''
        i = (low-1) #smaller element index
        pivot = array[high] #pivot value
        yield 'compare', array, None, None, high
        for j in range(low,high):
            if array[j] < pivot:
                i += 1
                yield 'compare', array, i, j, high
                array[i], array[j] = array[j], array[i]
                yield 'compare', array, i, j, high

        yield 'compare',array,  i+1, high, None
        array[i+1], array[high] = array[high], array[i+1]
        yield 'swapping', array, i+1, high, None

        pivot_index = i+1
        yield 'compare', array, None, None, pivot_index
        '''PARTITION FUNCTION END'''
        yield from quick_sort_helper(array, low, pivot_index-1)
        yield from quick_sort_helper(array, pivot_index+1, high)
