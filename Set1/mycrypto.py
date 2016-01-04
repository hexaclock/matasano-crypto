from Crypto.Cipher import AES
import base64
import sys
import os
import random
import hashlib

#xors two numbers
def xor(x,y):
	return x ^ y

#encodes a string in base64
def b64e(plain):
	return base64.b64encode(plain)
	
#decodes a base64 string	
def b64d(encoded):
	return base64.b64decode(encoded)
	
#decodes a hex string into text
def hextotext(s):
	return s.decode("hex")
	
#encodes a text string into hex
def texttohex(s):
	return s.encode("hex")
	
#converts str into ascii values, returns as array with each
def texttoascii(s):
	ret = [];
	for character in s:
		ret.append((ord(character)))
	return ret

#converts arr of ascii values to string of text
def asciitotext(arr):
	ret = ""
	for val in range(len(arr)):
		ret += chr(arr[val])
	return ret
	
#takes a string and length to
#pad up to. returns padded string
#of totlength
def pkcspad(string,totlength,padchar=chr(04)):
	padlength = totlength - len(string)
	return string+(padlength*padchar)
	
def nullpad(string,totlength,padchar=chr(0)):
	padlength = totlength - len(string)
	return string+(padlength*padchar)

#Return a string of n random bytes suitable for cryptographic use.
def getrandbytes(n):
	return os.urandom(n)
	
#Returns a random number in between start and end (inclusive).
def getrandnum(start,end):
	return random.randint(start,end)

#parses a line break separated text file into
#a list
def parsefile(filename):
	textfile = open(filename,"r")
	ret = textfile.read().split("\n")
	textfile.close()
	return ret
	
def parsefilestr(filename):
	textfile = open(filename,"r")
	ret = textfile.read().replace('\n','')
	textfile.close()
	return ret

#check if a list of ascii values is english or not given a threshold
#threshold is from 0 to 100
def checkenglish(asciilist,threshold):
	divisor = len(asciilist)
	lettercount = 0
	for i in range(len(asciilist)):
		if ( (asciilist[i] >= 97 and asciilist[i] <= 122) or (asciilist[i] >= 65 and asciilist[i] <= 90) or  (asciilist[i] == 32)):
			lettercount+=1
	if ( ((lettercount / float(divisor)) * 100) > threshold):
		return True
	else:
		return False
		
#takes a plaintext string and a key
#outputs the ciphertext
def xorencrypt(plaintext,key):
	plaintext = texttoascii(plaintext)
	key = texttoascii(key)
	ciphertext = []
	pos = 0
	for i in range(len(plaintext)):
		ciphertext.append(xor(plaintext[i],key[pos]))
		pos+=1
		if (pos == (len(key))):
			pos = 0
	return texttohex(asciitotext(ciphertext))
	
#takes a ciphertext string and a key
#outputs the plaintext
def xordecrypt(ciphertext,key):
	ciphertext = texttoascii(hextotext(ciphertext))
	key = texttoascii(key)
	plaintext = []
	pos = 0
	for i in range(len(ciphertext)):
		plaintext.append(xor(ciphertext[i],key[pos]))
		pos+=1
		if (pos == (len(key))):
			pos = 0
	return asciitotext(plaintext)
	
def genaeskey():
	return getrandbytes(16)
	
#takes a raw ciphertext string and a key
#outputs the plaintext
def aes_ecb_dec(ciphertext,key):
	plaintext = ""
	aesobj = AES.new(key,AES.MODE_ECB)
	for i in xrange(len(ciphertext)):
		if (i % 16 == 0):
			plaintext += aesobj.decrypt(ciphertext[i:i+16])
	return plaintext
	
def aes_ecb_enc(plaintext,key):
	ciphertext = ""
	aesobj = AES.new(key,AES.MODE_ECB)
	for i in xrange(len(plaintext)):
		if (i % 16 == 0):
			ciphertext += aesobj.encrypt(plaintext[i:i+16])
	return ciphertext
	
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