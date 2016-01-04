import sys
sys.path.append('../Set1/')

from mycrypto import *

def myxor(plaintext,key):
	plaintext = texttoascii(plaintext)
	key = texttoascii(key)
	ciphertext = []
	pos = 0
	for i in range(len(plaintext)):
		ciphertext.append(xor(plaintext[i],key[pos]))
		pos+=1
		if (pos == (len(key))):
			pos = 0
	return asciitotext(ciphertext)
	
def aes_cbc_enc(ptxt,key,iv):
	block = ptxt[0:16]
	xorblk = myxor(block,iv)
	ctxt = aes_ecb_enc(xorblk,key)
	for i in xrange(16,len(ptxt[16:])+1,16):
		block = ptxt[i:i+16]
		xorblk = myxor(block,ctxt[i-16:i])
		ctxt += aes_ecb_enc(xorblk,key)
	return ctxt

def aes_cbc_dec(ctxt,key,iv):
	block = ctxt[0:16]
	decblk = aes_ecb_dec(block,key)
	ptxt = myxor(decblk,iv)
	for i in xrange(16,len(ctxt[16:])+1,16):
		block = ctxt[i:i+16]
		decblk = aes_ecb_dec(block,key)
		ptxt += myxor(ctxt[i-16:i],decblk)
	return ptxt
	
def test():
	ciphertext = b64d(parsefilestr("10.txt"))
	plaintext = aes_cbc_dec(ciphertext,"YELLOW SUBMARINE",16*chr(00))
	ctxtcmp = b64e(aes_cbc_enc(plaintext,"YELLOW SUBMARINE",16*chr(00)))
	print plaintext
	print ctxtcmp == b64e(ciphertext)
