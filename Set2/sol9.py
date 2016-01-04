import sys
sys.path.append('../Set1/')

from mycrypto import *

#takes a string and length to
#pad up to. returns padded string
#of totlength
def pkcspad(string,totlength):
	padlength = totlength - len(string)
	return string+(padlength*chr(04))

print pkcspad("YELLOW SUBMARINE",20)