# Exercises 4.1
# Write out the code for the earlier sum function


def sum(arr):
    if not arr:
        return 0
    else:
        return arr.pop() + sum(arr)


if __name__ == "__main__":
    print(sum([2, 4, 6]))
