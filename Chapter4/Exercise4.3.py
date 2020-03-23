# Exercise 4.3
# Find the maximum number in a list


def maximum_number(arr):
    """My recursive solution"""
    if not arr:
        return 0
    else:
        sub_max = maximum_number(arr[1:])
        if arr[0] > sub_max:
            return arr[0]
        else:
            return sub_max


def max(arr):
    """The book author's solution"""
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max


if __name__ == "__main__":
    print("Maximum number is: ", maximum_number([10, 15, 1, 3, 22]))
    print("Maximum number is: ", max([10, 15, 1, 3, 22]))
