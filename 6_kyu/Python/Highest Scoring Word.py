"""
	- Instruction! -

	Given a string of words, you need to find the highest scoring word.
	Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
	You need to return the highest scoring word as a string.
	If two words score the same, return the word that appears earliest in the original string.
	All letters will be lowercase and all inputs will be valid.

"""

def high(x):
    word, max_w, arr = " ", 0 ,'abcdefghijklmnopqrstuvwxyz'
    for i in x.split(" "):
        summ = sum([arr.index(symb)+1 for symb in i])
        if summ > max_w: 
            max_w = summ
            word = i
    return word
