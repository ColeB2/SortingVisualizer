'''
algorithms.py
algorithm information and help received from website: geeksforgeeks.org
'''
'''Bubble Sort'''
def bubble_sort(array):
    n = len(array)
    for pass_num in range(n-1, 0, -1):
        for j in range(pass_num):
            yield 0, j, j+1, array
            if array[j] > array[j+1]:
                yield 1, j, j+1, array
                array[j], array[j+1] = array[j+1], array[j]
                yield 2, j, j+1, array

def fast_bubble_sort(array):
    n = len(array)
    for pass_num in range(n-1, 0, -1):
        swap = False
        for j in range(pass_num):
            yield 0, j, j+1, array
            if array[j] > array[j+1]:
                swap = True
                yield 1, j, j+1, array
                array[j], array[j+1] = array[j+1], array[j]
                yield 2, j, j+1, array


        if swap == False:
            print('Done')
            raise StopIteration()

'''Selection Sort'''
def selection_sort(array):
    n = len(array)
    for fill_slot in range(n-1, 0, -1):
        position_max = 0
        yield 0, position_max, None, array
        for location in range(1, fill_slot + 1):
            yield 0, position_max, location, array
            if array[location] > array[position_max]:
                position_max = location
                yield 0, position_max, None, array

        yield 0, fill_slot, position_max, array
        (array[fill_slot],
        array[position_max]) = (array[position_max],
        array[fill_slot])
        yield 1, fill_slot, position_max, array
        #yield 2, None, None, array

'''Insertion Sort'''
def insertion_sort(array):
    print('INSERT SORT 1')
    n = len(array)
    yield 4, None, None, 0, array
    for i in range(1, n, 1):
        item = array[i]
        j = i - 1
        yield 3, None, None, i, array
        while j >= 0 and item < array[j]:
            yield 4, j+1, j, i, array
            array[j+1], array[j] = array[j], array[j+1]
            '''
            swap j+1, j for visualization purposes
            isntead of pulling the value out, moving all them up, then inserting
            '''
            yield 4, j+1, j, i, array

            j-=1
        array[j+1] = item

        yield 2, None, None, array

'''Shell Sort'''
def shell_sort(array):
    n = len(array)

    gap = n // 2

    while gap > 0:
        yield 2, None, None, array
        for i in range(gap, n):
            temp = array[i]

            j = i
            while j >= gap and array[j-gap] > temp:
                yield 0, j, j-gap, array
                array[j] = array[j-gap]
                yield 1, j, j-gap, array
                j-= gap

            array[j] = temp
            yield 2, i, None, array

        gap //= 2


'''Heap Sort'''
def heap_sort(array):
    n = len(array)
    '''BUILDINGMAXHEAP FUNCTION'''
    for i in range(n):
        #yield 2, None, None, array
        '''if arr[i](child) > arr[x]parent:'''
        if array[i] > array[int((i - 1) / 2)]:
            j = i
            while array[j] > array[int((j - 1) / 2)]:
                yield 0, j, int((j-1)/2), array
                (array[j],
                 array[int((j - 1) / 2)]) = (array[int((j - 1) / 2)],
                                           array[j])
                yield 1, int((j-1)/2), j, array
                j = int((j - 1) / 2)
                yield 2, None, None, array

    '''HEAP SORT'''
    yield 2, None, None, array
    for i in range(n - 1, 0, -1):
        yield 0, i, 0, array
        array[0], array[i] = array[i], array[0]
        yield 1, i, 0, array

        j, index = 0, 0

        while True:
            index = 2 * j + 1

            if (index < (i - 1) and
                array[index] < array[index + 1]):
                index += 1

            if index < i and array[j] < array[index]:
                yield 0, index, j, array
                array[j], array[index] = array[index], array[j]
                yield 2, index, j, array

            j = index
            if index >= i:
                break
'''Merge Sort, adjust fromed code @'''
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
                    yield 0, m-1, m, array
                    array[m-1], array[m] = array[m], array[m-1]
                    yield 1, m-1, m, array
            n -= 1

def wmerge(array, i, m, j, n, w):
    """
    Merge subarrays [i, m) and [j, n) into work area w.
    All indexes point into array.
    The space after w must be enough to fit both subarrays.
    """
    while i < m and j < n:
        if array[i] < array[j]:
            yield 0, i, w, array
            array[i], array[w] = array[w], array[i]
            yield 1, i, w, array
            i += 1
        else:
            yield 0, j, w, array
            array[j], array[w] = array[w], array[j]
            yield 1, j, w, array
            j += 1
        w += 1
    while i < m:
        yield 0, i, w, array
        array[i], array[w] = array[w], array[i]
        yield 1, i, w, array
        i += 1
        w += 1
    while j < n:
        yield 0, j, w, array
        array[j], array[w] = array[w], array[j]
        yield 1, j, w, array
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
            yield 0, l, w, array
            array[l], array[w] = array[w], array[l]
            yield 1, l, w, array
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
        yield 3, None, None, high, array
        for j in range(low,high):
            if array[j] < pivot:
                i += 1
                yield 3, i, j, high, array
                array[i], array[j] = array[j], array[i]
                yield 3, i, j, high, array

        yield 3, i+1, high, None, array
        array[i+1], array[high] = array[high], array[i+1]
        yield 4, i+1, high, None, array

        pivot_index = i+1
        yield 3, None, None, pivot_index, array
        '''PARTITION FUNCTION END'''
        yield from quick_sort_helper(array, low, pivot_index-1)
        yield from quick_sort_helper(array, pivot_index+1, high)
