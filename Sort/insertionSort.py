## Insertion Sort

def insertionSort(arr):
	for i in range(len(arr)):
		j = i-1
		key = arr[i]

		while(j >= 0 and key < arr[j]):
			arr[j+1] = arr[j]
			j = j-1
		arr[j+1] = key
	return arr

## Driver Code

arr = [75, 100, 90, 95, 80]
print(insertionSort(arr))

