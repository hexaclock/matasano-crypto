from mycrypto import *

def sol():
	ctxtl = parsefile("8.txt")
	for i in xrange(len(ctxtl)):
		chunks = []
		for j in xrange(0,len(ctxtl[i]),16):
			chunks.append(ctxtl[i][j:j+16])
		duplicates = len(chunks) - len(set(chunks))
		if duplicates > 0:
			print("Line: "+str(i+1))
			print("Possible AES-ECB ciphertext detected: "+ctxtl[i])
	
sol()