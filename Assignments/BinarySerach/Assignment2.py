"""
Assignment#3:

Given a positive integer num, write a program that returns True if num is a perfect
square else return False. Do not use built-in functions like sqrt. Also, talk about the time
complexity of your code.
Test Cases:
Input: 16
Output: True
Input: 14
Output: False
"""
## Function Formation

def binarySearch(x, start, end):

	while(start <= end):

		mid = start + (end - start)//2

		if mid * mid == x:
			return True
		elif mid * mid < x:
			start = mid + 1
		elif mid * mid > x:
			end = mid - 1

	return False


## Driver code

x = 26

print(binarySearch(x, 1, x))
