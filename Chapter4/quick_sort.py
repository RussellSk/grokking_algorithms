# Chapter 4
# Quick sort implementation


def quicksort(array):
    if len(array) < 2:
        return array  # Base case: arrays with 0 or 1 element are already "sorted".
    else:
        pivot = array[0]  # Recursive case
        less = [i for i in array[1:] if i <= pivot]  # Sub-array of all the elements less than the pivot
        greater = [i for i in array[1:] if i > pivot]  # Sub-array of all the elements greater than the pivot
        return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == "__main__":
    array = [10, 5, 3, 2, 4, 6, 8, 7, 9, 1]
    print("Unsorted array: ", array)
    array = quicksort(array)
    print("Sorted array: ", array)

