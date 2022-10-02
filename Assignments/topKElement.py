## Find Top k number of elemnets using heap sort

import heapq
from collections import Counter
## Function Definition

def topKelements(arr, k):
	if len(arr) == k:
		return set(arr)
	count = Counter(arr)
	print(count)
	return heapq.nlargest(k, count.keys(), count.get)

## Driver Code
arr = [1,1,1, 2, 2, 3,3,3,4,4]
k = 2
print(topKelements(arr, k))