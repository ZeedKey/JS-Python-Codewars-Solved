/**
	- Instruction! -

	Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
	It should remove all values from list a, which are present in list b keeping their order.

**/

//JS
function arrayDiff(a, b) {
  return a.filter((el) => b.includes(el) == false)
}

/**
Python

def array_diff(a, b): return [i for i in a if i not in b]

**/