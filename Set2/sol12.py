import sys
sys.path.append('../Set1/')
from mycrypto import *

def aes_ecb_oracle(ptxt):
	h = hashlib.sha1()
	h.update('YELLOW SUBMARINE')
	AESKEY = h.digest()[0:16]

	string = ptxt + b64d("Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK")
	#print b64d("Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK")
	padlen = len(string) + 16 - (len(string)%16)
	rndpad = pkcspad(string,padlen)
	return aes_ecb_enc(rndpad,AESKEY)
	
def isecb():
	ctxtl = aes_ecb_oracle("YELLOW SUBMARINEYELLOW SUBMARINEYELLOW SUBMARINEYELLOW SUBMARINEYELLOW SUBMARINEYELLOW SUBMARINEYELLOW SUBMARINEYELLOW SUBMARINEYELLOW SUBMARINEYELLOW SUBMARINEYELLOW SUBMARINE")
	chunks = []
	for j in xrange(0,len(ctxtl),16):
		chunks.append(ctxtl[j:j+16])
	duplicates = len(chunks) - len(set(chunks))
	if duplicates > 0:
		return True
	return False

def guessblksize():
	blocksize = None
	for bs in xrange(1,20):
		plaintext = 'A'*bs*100
		enc = aes_ecb_oracle(plaintext)
		block = enc[bs:2*bs]
		if enc[:bs] == block:
			blocksize = bs
			break
	print('guessing blocksize is %s' % blocksize if blocksize else 'no blocksize found')
	if blocksize is None: return # no point continuing

def sol():	
	#print aes_ecb_oracle()
	found = ""
	lgth = 144
	for i in xrange(lgth-1,0,-1):
		rbt = dict()
		inputblk = "A"*i
		for j in range(256):
			rbt[aes_ecb_oracle(inputblk+found+chr(j))[0:lgth]] = chr(j)
		found += rbt[aes_ecb_oracle(inputblk)[0:lgth]]
	print found

sol()