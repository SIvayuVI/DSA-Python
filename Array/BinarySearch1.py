##Two Pointer approach
## Find out a,b which gives sum as equal to c
arr = [20, 30, 40, 50, 60, 70, 80]
sum_value = 130
r = len(arr) - 1
l = 0

def binarySearch(r, l):
	
	while l < r:
		if (arr[r] + arr[l]) == sum_value:
			return arr[r], arr[l]
		elif (arr[r] + arr[l]) > sum_value:
			r = r - 1
		elif (arr[r] + arr[l]) < sum_value:
			l = l - 1
	return -1

print(binarySearch(r, l))