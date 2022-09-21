#Bubble Sort
def bubbleSort(arr):
	n = len(arr)
	for i in range(n):
		for j in range(0, n-i-1):
			#n-i-1 - > Every pass the last element always be sort
			if arr[j] > arr[j+1]: # > used for asc and < used for desc orders
				#Swap
				arr[j], arr[j+1] = arr[j+1], arr[j]
	return arr

## Driver code
arr = [10,50, 60, 80, 70, 90, 20]
print(bubbleSort(arr))