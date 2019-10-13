
from random import sample


def quick_sort(array):
    if len(array) > 1:
        pivot = array[-1]
        low = []
        high = []
        for elem in array[:-1]:
            if elem > pivot:
                high.append(elem)
            elif elem <= pivot:
                low.append(elem)
        low = quick_sort(low)
        high = quick_sort(high)
        return swap(pivot, low, high)
    else:
        return array


def swap(pivot, low, high):
    return(low + [pivot] + high)


unsorted_array_1 = sample(range(10), 10)
unsorted_array_2 = sample(range(10), 10)
print(f"Unsorted array numb. 1:\n {unsorted_array_1}")
print(quick_sort(unsorted_array_1))
print(f"Unsorted array numb. 2:\n{unsorted_array_2}")
print(quick_sort(unsorted_array_2))
