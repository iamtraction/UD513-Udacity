"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    sort(array, 0, len(array) - 1)
    return array

def sort(array, lo, hi):
    if lo < hi:
        p = partition(array, lo, hi)
        sort(array, lo, p - 1)
        sort(array, p + 1, hi)

def partition(array, lo, hi):
    pivot = array[hi]
    i = lo
    for j in range(lo, hi):
        if array[j] < pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[hi] = array[hi], array[i]
    return i

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)
