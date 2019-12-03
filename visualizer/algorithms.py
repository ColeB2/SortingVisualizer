'''
algorithms.py
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


'''Merge Sort'''
def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i=0
        j=0
        k=0

        yield 2, None, None, array
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                yield 3, k, i, j, array
                array[k] = left_half[i]
                yield 4, k, i, j, array
                i = i + 1
            else:
                yield 3, k, j, i, array
                array[k] = right_half[j]
                yield 4, k, j, i, array
                j = j + 1
            k = k + 1

        while i < len(left_half):
            yield 3, k, i, j, array
            array[k] = left_half[i]
            yield 4, k, i, j, array
            i = i + 1
            k = k + 1

        while j < len(right_half):
            yield 3, k, j, i, array
            array[k] = right_half[j]
            yield 4, k, j, i, array
            j = j + 1
            k = k + 1
'''Quick Sort'''
