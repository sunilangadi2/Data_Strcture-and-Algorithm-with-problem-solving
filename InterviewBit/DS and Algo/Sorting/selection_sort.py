'''The selection sort algorithm sorts an array 
by repeatedly finding the minimum element (considering ascending order) 
from unsorted part and putting it at the beginning.

Time Complexity: O(n2) as there are two nested loops.'''


def selection_sort(array):
    n = len(array)
    for i in range(n):
        mini = i
        for j in range(i + 1, n):
            if array[j] < array[mini]:
                mini = j
        array[i], array[mini] = array[mini], array[i]
    return array


a = [23, 4, 5, 1, 345, 89, 7]
print selection_sort(a)
