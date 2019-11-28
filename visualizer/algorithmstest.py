import algorithms
import random
from colorama import Fore, Style

def create_array(size=20):
    arr = list()
    for i in range(size):
        arr.append(random.randint(0, 100))

    return arr

def force_fail(algo):
    yield False

def copy_array(array):
    new_array = list()
    for item in array:
        new_array.append(item)
    return new_array

def test_algo(algo, array1=None, array2=None):
    array1 = create_array()
    array2 = copy_array(array1)
    array2.sort()
    x = algo(array1)
    while True:
        try:
            next(x)
        except:
            break
    if array1 == array2:
        return array1 == array2
    else:
        return False

def TEST_INFO(algo):
    print(Fore.CYAN)
    print("Testing", end=' : ')
    print(algo)
    print(Style.RESET_ALL, end='')


def TEST(algo):
    #TEST_INFO(algo)
    testFunc = test_algo(algo)
    if testFunc == True:
        print(Fore.GREEN + 'Passed:', end=' ')
        print(Style.RESET_ALL, end='')
        print(str(algo))
    else:
        print(Fore.RED + 'Failed:', end=' ')
        print(Style.RESET_ALL, end='')
        print(str(algo))


if __name__ == '__main__':
    TEST(force_fail)
    TEST(algorithms.bubble_sort)
    TEST(algorithms.heap_sort)
