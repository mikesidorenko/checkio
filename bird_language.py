VOWELS = "aeiouy"

def translate(phrase):
	import re #importing re module to use regex on the next line
	phrase = re.sub(r'(?<=[^aeiouy\s])([aieouy])', '', phrase) 
	#removed vowels after consonants

	for vow in VOWELS: #iterating vowels and replacing triple ones with single ones
		triple = vow * 3
		phrase = phrase.replace(triple, vow)
	return phrase