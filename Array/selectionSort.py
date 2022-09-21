## Selection Sort

def selectionSort(arr):
	n = len(arr)
	
	for i in range(n):
		min_idx = i
		for j in range(i+1, n):
			if arr[j] < arr[min_idx]:
				min_idx = j
		arr[i], arr[min_idx] = arr[min_idx], arr[i] 
	return arr

## Driver code
arr = [10,50, 60, 80, 70, 90, 20]
print(selectionSort(arr))

