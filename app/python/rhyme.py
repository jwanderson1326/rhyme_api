from pronouncing import rhymes

def get_rhymes(word):
	word2 = str(word).strip().lower()
	if rhymes(word2) == []:
		rhymelist = 'None - Is that an English word?'
	else:
		rhymelist = rhymes(word2) 

	return rhymelist