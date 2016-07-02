import unittest

def deHash(code):
	
	letters = "acdegilmnoprstuw"
	letters = list(letters)
	
	decrypt = []
	word = []
	
	while(code>7):
		rem = code%37
		code = code/37
		decrypt.append(rem)
	
	for i in decrypt:
		try:
			word.append(letters[i])
		except IndexError:
			print "Hash has letters outside pre-defined list."
	result_string = "".join(word)[::-1]
	return result_string

class TestCases(unittest.TestCase):
	def testCode(self):
		self.assertEqual(deHash(930846109532517), "lawnmower")
		self.assertEqual(deHash(680131659347), "leepadg")

unittest.main()


