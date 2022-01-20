"""
	- Instruction! -

	How can you tell an extrovert from an introvert at NSA? Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.
	I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it? According to Wikipedia, ROT13 (http://en.wikipedia.org/wiki/ROT13) is frequently used to obfuscate jokes on USENET.
	Hint: For this task you're only supposed to substitue characters. Not spaces, punctuation, numbers etc. Test examples:

"""

def rot13(m):
    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    rotalph = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
    new_str = ""
    for i in m:
        if i in alph: new_str+=alph[rotalph.index(i)]
        else: new_str+=i
    return new_str
