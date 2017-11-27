from random import randint

def return_random(words):
	wordlist = [word for word in str(words).split(' ') if word != ""]
	chosen = wordlist[randint(0,len(wordlist)-1)] 
	return chosen