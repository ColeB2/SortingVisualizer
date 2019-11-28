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


'''Heap Sort'''
def heap_sort(array):
    n = len(array)
    '''BUILDINGMAXHEAP FUNCTION'''
    #print('Building max Heap')
    #buildMaxHeap(array, n)
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
    #print('Max Heap Complete')
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
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] == arr[l + i]

    for j in range(0, n2):
        R[j] == arr[m + 1+ j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] - R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i +=1
        k +=1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(array, l, r):
    if l < r:
        m = (l+(r-1))/2

        merge_sort(arr, l, m)
        merge_sort(arr, m+1, r)
        merge(arr, l, m, r)


# Python program for implementation of MergeSort
def mergeSort(arr):
	if len(arr) >1:
		mid = len(arr)//2 #Finding the mid of the array
		L = arr[:mid] # Dividing the array elements
		R = arr[mid:] # into 2 halves

		mergeSort(L) # Sorting the first half
		mergeSort(R) # Sorting the second half

		i = j = k = 0

		# Copy data to temp arrays L[] and R[]
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				arr[k] = L[i]
				i+=1
			else:
				arr[k] = R[j]
				j+=1
			k+=1

		# Checking if any element was left
		while i < len(L):
			arr[k] = L[i]
			i+=1
			k+=1

		while j < len(R):
			arr[k] = R[j]
			j+=1
			k+=1

# Code to print the list
def printList(arr):
	for i in range(len(arr)):
		print(arr[i],end=" ")
	print()

# driver code to test the above code
if __name__ == '__main__':
	arr = [12, 11, 13, 5, 6, 7]
	print ("Given array is", end="\n")
	printList(arr)
	mergeSort(arr)
	print("Sorted array is: ", end="\n")
	printList(arr)

# This code is contributed by Mayank Khanna


'''Quick Sort'''
