## TO find Min and Max of array using Divide and Conqure ALgorithm

## Function Definition:

def findMaxAndMin(arr, i, j, min, max):

	if i == j:
		## If there is a single index
		min = arr[i]
		max = arr[j]
		return min, max

	elif i == j-1:
		## If there is a two index
		if arr[i] < arr[j]:
			min = arr[i]
			max = arr[j]
		elif arr[i] < arr[j]:
			min = arr[j]
			max = arr[i]
		else:
			min = arr[i]
			max = arr[i]
		return min, max

	else:
		## if there is a multiple index
		mid = i + (j-i)//2
		min_1, max_1 = findMaxAndMin(arr, i, mid, min, max)
		min_2, max_2 = findMaxAndMin(arr, mid+1, j, min, max)

		if min_1 < min_2:
			min = min_1
		else:
			min = min_2
		if max_1 > max_2:
			max = max_1
		else:
			max = max_2
		return min, max

## Driver code

arr = [2,4,1,7,9,3,5,10]
min = float('inf')
max = 0
print(findMaxAndMin(arr, 0, len(arr)-1, min, max))