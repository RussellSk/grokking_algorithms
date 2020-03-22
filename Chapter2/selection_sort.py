def findSmallest(arr):
    """Function to find the smallest element"""
    smallest = arr[0]  # Stores the smallest value
    smallest_index = 0  # Stores the index of the smallest value
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    """Selection sort"""
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)  # Finds the smallest element in the array, and add it to the new array
        newArr.append(arr.pop(smallest))  # Return element from arr and then remove it
    return newArr


if __name__ == "__main__":
    arr = [5, 3, 6, 2, 10]
    print("Array before sorting: ", arr)
    print("Array after sorting: ", selectionSort(arr))
