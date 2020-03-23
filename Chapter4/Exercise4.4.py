# Exercise 4.4
# Remember binary search from chapter 1? It's a divide-and-conquer algorithm, too.
# Can you come up with the base case and recursive case for binary search?


def recursive_binary_search(arr, item):
    if len(arr) == 1:
        return "Found!" if arr[0] == item else None
    mid = len(arr) // 2
    if arr[mid] > item:
        return recursive_binary_search(arr[0:mid], item)
    else:
        return recursive_binary_search(arr[mid:], item)


if __name__ == "__main__":
    # binary search only works with sorted array
    print("Recursive binary search: ", recursive_binary_search([1, 2, 3, 4, 5, 6, 7, 8], 8))
