"""
	- Instruction! -

	Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are substrings of strings of a2.

"""

def in_array(a1, a2):
    arr = []
    for substr in a1:
        for string in a2:
            if substr in string: arr.append(substr)
    return list(sorted(set(arr)))
