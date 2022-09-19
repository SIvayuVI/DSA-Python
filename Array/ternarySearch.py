## Function Definition
def ternarySearch(arr, l, r, x):

    while l <= r:
        mid_1 = l + (r - l)//3
        mid_2 = r - (r - l)//3
        if arr[mid_1] == x:
            return mid_1
        elif arr[mid_2] == x:
            return mid_2
        elif arr[mid_1] > x:
            return ternarySearch(arr, l, mid_1-1, x)
        elif arr[mid_2] < x:
            return ternarySearch(arr, mid_2 + 1, r, x)
        else:
            return ternarySearch(arr, mid_1 + 1, mid_2 - 1, x)
    return -1

## Driver Code
arr = [23, 25, 27, 45, 39, 60, 75, 80, 89]
x = 75
print(ternarySearch(arr, 0, len(arr)-1, x))

