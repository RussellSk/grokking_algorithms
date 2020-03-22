def binary_search(list, item):
    # low and high keep track of which part of the list you'll search
    low = 0
    high = len(list) - 1

    while low <= high:  # While you haven't narrowed it down to one element...
        mid = (low + high) // 2  # ... check the middle element
        guess = list[mid]
        if guess == item:  # Found the item
            return mid
        if guess > item:  # The guess was too high
            high = mid - 1
        else:  # The guess was too low
            low = mid + 1

    return None  # Item doesn't exist in list


if __name__ == '__main__':
    list_of_digits = [10, 92, 15, 46, 58, 17, 63, 84, 91, 25]
    print("Unsorted list: ", list_of_digits)
    list_of_digits.sort()  # binary_search only works with sorted list
    print("Sorted list: ", list_of_digits)
    print(binary_search(list_of_digits, 25))
