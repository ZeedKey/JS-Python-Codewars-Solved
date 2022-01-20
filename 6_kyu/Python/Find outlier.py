"""
	- Instruction! -

	You are given an array (which will have a length of at least 3, but could be very large) containing integers. 
	The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. 
	Write a method that takes the array as an argument and returns this "outlier" N.
"""

def find_outlier(ints):
    arr = [i for i in ints if i%2==0]
    if len(arr) == 1: return arr[0]
    else: return [i for i in ints if i%2!=0][0]

