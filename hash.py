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
	print result_string

def main():
	string = "leepadg"
	code = 930846109532517
	deHash(code)


if __name__== "__main__":
	main()

