"""
Assignment #1
Compute and return the square root of x, where x is guaranteed to be a non-negative
integer. And since the return type is an integer, the decimal digits are truncated and only
the integer part of the result is returned. Also, talk about the time complexity of your
code.
Test Cases:
Input: 4
Output: 2
Input: 8
Output: 2
Explanation: The square root of 8 is 2.8284…., the decimal part is truncated and 2 is
returned.
"""
## Function for BinarySearch

def binarySearch(x, start, end):

	mid  = start + (end - start)//2

	if start > end: 
		return False
	if mid * mid == x: 
		return True
	elif mid * mid < x:
		return binarySearch(x, mid + 1, end)
	elif mid * mid > x: 
		return binarySearch(x, start, mid - 1)

## Driver code

x = 25
print(binarySearch(x, 1, x))