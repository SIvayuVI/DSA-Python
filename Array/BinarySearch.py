def binarySearch(arr, x, i, j):
	while(True):
		mid = i + (j-i)//2
		if arr[mid] == x:
			return mid
		elif arr[mid] < x:
			i = mid + 1
		else:
			j = mid - 1
	return -1

arr = [20, 30, 40, 50, 60, 70]
x = 50
i = 0
j = len(arr) - 1
result = binarySearch(arr, x, i, j)
print("The Search Index is : ", result)

	
