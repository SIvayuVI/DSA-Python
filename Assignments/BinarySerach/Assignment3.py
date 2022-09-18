"""
Assignment#2 
You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check. Since each
version is developed based on the previous version, all the versions after a bad version
are also bad. Suppose you have n version and you want to find out the first bad one,
which causes all the following ones to be bad. Also, talk about the time complexity of
your code.
Test Cases:
Input: [0,0,0,1,1,1,1,1,1]
Output: 3
Explanation: 0 indicates a good version and 1 indicates a bad version. So, the index of
the first 1 is at 3. Thus, the output is 3
"""
x = [0,0,0,1,1,1,1,1,1]

def binarySearch(x):
	start = 1
	end = len(x) - 1

	while start < end:
		mid = start + (end - start)//2

		if x[mid] == 1:
			end =  mid
		else:
			start = mid + 1

	return start

print(binarySearch(x))