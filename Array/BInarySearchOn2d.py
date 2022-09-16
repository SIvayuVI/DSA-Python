def binarySearch(arr, i, j, n, m):
	## Implementation
	while i <= j:

		mid = i + ((j-i)//2)
		mid_row = mid // n
		mid_column = mid % n
		mid_element = arr[mid_row][mid_column]

		if mid_element == x:
			return mid_row, mid_column
		elif mid_element < x:
			i = mid + 1
		elif mid_element > 1:
			j = mid -1

	return -1

## Driver Code
arr = [[1, 2, 3, 5], [7, 8, 10, 12], [14, 17, 18, 20]]
i = 0 # Start index
x = 17 # Search number
n = len(arr[0]) # Number of columns
m = len(arr) # Number of rows
j = (m * n) - 1 # end index

print(binarySearch(arr, i, j, n, m))

