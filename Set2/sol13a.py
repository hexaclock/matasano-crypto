import sys
import math
sys.path.append('../Set1/')
from mycrypto import *

def myround(x, base=16):
	if x%16 == 0:
		return x
	return 16 + int(base * round(float(x)/base))

#Parses k=v into a JSON-like object
#foo=bar&baz=qux&zap=zazzle 
# ==> 
#{
#  foo: 'bar',
#  baz: 'qux',
#  zap: 'zazzle'
#}
def kvparse(kvstr):
	ret = "{\n "
	for c in kvstr:
		if c == '=':
			ret += ": '"
		elif c == '&':
			ret += "',\n "
		else:
			ret += c
	ret += "'\n}"
	return ret

#input: email address (ex: dvinak@gmail.com)
#output: "email=dvinak@gmail.com&uid=10&role=user"
def profile_for(email,usertype="user"):
	cleanemail = ""
	for c in email:
		if (c != '&' and c != '='):
			cleanemail += c
	kvstr = "email="+cleanemail+"&uid=10"+"&role="+usertype
	return kvstr
	
def silly_enc(ptxt):
	key = b64d("Zni1WBbKoMdbzNGIUcsgRA==")
	padded = pkcspad(ptxt,myround(len(ptxt)))
	return aes_ecb_enc(padded,key)
	
def silly_dec(ctxt):
	key = b64d("Zni1WBbKoMdbzNGIUcsgRA==")
	return aes_ecb_dec(ctxt,key)

myprofile = silly_enc(profile_for("fooxz@bar.com"))
#force admin to appear in 2nd block
admin = silly_enc(profile_for('A'*10 + 'admin' + chr(0)*11))
print silly_dec(myprofile[0:32]+admin[16:32])
#print kvparse(silly_dec(silly_enc(profile_for("dvinak@gmail.com"))))