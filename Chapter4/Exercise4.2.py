# Exercise 4.2
# Write a recursion function to count the number of items in a list


def count(arr):
    if not arr:
        return 0
    else:
        return 1 + count(arr[1:])


if __name__ == "__main__":
    print(count([1, 2, 3, 4, 5]))