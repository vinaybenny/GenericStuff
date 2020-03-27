""" A bunch of simple implementations of sort/binary search algorithms in both recursive and 
    non-recursive modes for numpy arrays. The implementations here are for -
        1. Insertion Sort
        2. Recursive Insertion Sort
        3. Binary Search
        4. Binary Insertion Sort
        5. Recursive Merge Sort
"""

import numpy as np

def insertion_sort(nparray):
    for i in range(1, len(nparray)):
        if nparray[i] < nparray[i - 1]:
            for j in range(-i, 0):
                k = -j
                if nparray[k] < nparray[k-1]:
                    temp = nparray[k-1]
                    nparray[k-1] = nparray[k]
                    nparray[k] = temp
    return nparray


def insertion_sort_recurse(nparray):    
    if len(nparray) == 1:
        return nparray
        
    for i in range(1, len(nparray)):   
        if nparray[i] < nparray[i-1]:
            temp = nparray[i-1]
            nparray[i-1] = nparray[i]
            nparray[i] = temp
            nparray = np.concatenate((insertion_sort_recurse(nparray[0:i]), nparray[i:len(nparray)]))
    return nparray


def binary_search(element, sortedarray):
    
    if element > sortedarray[len(sortedarray) - 1]:
        return len(sortedarray)
    elif element < sortedarray[0]:
        return 0
    elif sortedarray[np.int(len(sortedarray)/2) - 1] == element:
        return np.int(len(sortedarray)/2) - 1
    elif sortedarray[np.int(len(sortedarray)/2) - 1] < element:
        return np.int(len(sortedarray)/2) + binary_search(element, sortedarray[np.int(len(sortedarray)/2):len(sortedarray)])
    else:
        return binary_search(element, sortedarray[0: np.int(len(sortedarray)/2)])
        

        
def binary_insertion_sort(nparray):
    for i in range(1, len(nparray)):
        
        if nparray[i] < nparray[i - 1]:            
            nparray = np.insert(nparray, binary_search(nparray[i], nparray[:i]), nparray[i])
            nparray = np.delete(nparray, [i+1])
    return nparray


def merge_sort_recurse(nparray):
    
    if len(nparray) == 1:
        return nparray
    else:
        left, right = merge_sort_recurse(nparray[0:np.int(len(nparray)/2)]), merge_sort_recurse(nparray[np.int(len(nparray)/2):len(nparray)])
        i = 0
        j = 0
        outarray = np.zeros(len(left) + len(right))
        while i + j < len(left) + len(right):
            if j < len(right) and (i >= len(left) or left[i] > right[j]):
                outarray[i + j] = right[j]
                j = j + 1
            elif  i < len(left) and (j >= len(right) or left[i] <= right[j]):
                outarray[i + j] = left[i]
                i = i + 1
                       
        return outarray

def test_sorting():
    a = np.random.randint(100, size=(1,20))[0]
    print(a)
    print("Merge Sort Output: ", merge_sort_recurse(a))
    
    a = np.random.randint(100, size=(1,20))[0]
    print(a)
    print("Binary Insertion Sort Output: ", binary_insertion_sort(a))
    
    a = np.random.randint(100, size=(1,20))[0]
    print(a)
    print("Recursive Insertion Sort Output: ", insertion_sort_recurse(a))
    
    a = np.random.randint(100, size=(1,20))[0]
    print(a)
    print("Insertion Sort Output: ", insertion_sort(a))

if __name__ == "__main__":
    test_sorting()




