from mycrypto import *

ciphertext = b64d(parsefilestr("7.txt"))
key = "YELLOW SUBMARINE"
plaintext = aes_ecb_dec(ciphertext,key)
print b64e(aes_ecb_enc(plaintext,key)) == b64e(ciphertext)