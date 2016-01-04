import sys
sys.path.append('../Set1/')

from mycrypto import *

def genaeskey():
	return getrandbytes(16)

def encryption_oracle(ptxt):
	key = genaeskey()
	string = getrandbytes(getrandnum(5,11)) + ptxt + getrandbytes(getrandnum(5,11))
	padlen = len(string) + 16 - (len(string)%16)
	rndpad = pkcspad(string,padlen)
	if (getrandnum(0,1) == 0):
		print "DOING AES-ECB"
		return aes_ecb_enc(rndpad,key)
	else:
		print "DOING AES-CBC"
		iv = getrandbytes(16)
		return aes_cbc_enc(rndpad,key,iv)
		
def isecb():
	ctxtl = encryption_oracle("YELLOW SUBMARINEYELLOW SUBMARINEYELLOW SUBMARINEYELLOW SUBMARINEYELLOW SUBMARINEYELLOW SUBMARINEYELLOW SUBMARINEYELLOW SUBMARINEYELLOW SUBMARINEYELLOW SUBMARINEYELLOW SUBMARINE")
	chunks = []
	for j in xrange(0,len(ctxtl),16):
		chunks.append(ctxtl[j:j+16])
	duplicates = len(chunks) - len(set(chunks))
	if duplicates > 0:
		return True
	return False

#print b64e(encryption_oracle("AESAESAESAESAESAESAESAESAESAESAESAESAESAESAESAESAESAESAESAESAESAESAESAESAES"))
print isecb()