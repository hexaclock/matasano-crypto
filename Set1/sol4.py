#solution to number 3: "Cooking MC's like a pound of bacon"
from mycrypto import *
#returns a list of 30 lists, each containing 128 numbers representing
#all possible xors for each character
def scxbrute(ascii_value_list):
	allxors = [];
	#for every ascii value in the list
	for i in range(128):
		singlexor = []
		for ascval in range( len(ascii_value_list) ):
			#xor it with 0..127
			singlexor.append(xor(ascii_value_list[ascval],i))
		allxors.append(singlexor)		
	return allxors
	
def solve4():
	data = parsefile("4.txt")
	ordered = []
	for i in range(len(data)):
		ordered.append(scxbrute(texttoascii(hextotext(data[i]))))
	for i in range(len(ordered)):
		for j in range(len(ordered[i])):
			if (checkenglish(ordered[i][j],90)):
				print data[i]
				print "xor'ed with: "+chr(j)+" is:"
				print asciitotext(ordered[i][j])

def verify4():
	plaintext = texttoascii("Now that the party is jumping\n")
	key = texttoascii('5')[0]
	ciphertext = []
	for i in range(len(plaintext)):
		ciphertext.append(xor(plaintext[i],key))
	print "Now that the party is jumping"
	print "xor'ed with: "+str(chr(key))+" is:"
	print texttohex(asciitotext(ciphertext))
	
solve4()