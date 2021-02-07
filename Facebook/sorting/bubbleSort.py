def bubbleSort(array):
    sorted = False
    counter = 0
    while not sorted:
        sorted = True
        for i in range(len(array)-1-counter):
            if array[i] > array[i + 1]:
                swap(i, i + 1, array)
                sorted = False
        counter += 1
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

import pytest

def test_shortArray():
    a = [3,2,1]
    assert [1,2,3] == bubbleSort(a)

def test_longArray():
    a = [3,4,-6,2,1,4,6,-2,-3,0]
    assert [-6, -3, -2, 0, 1, 2, 3, 4, 4, 6 ] == bubbleSort(a)