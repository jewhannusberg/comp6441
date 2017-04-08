"""
The Base64-encoded content in aes128_ciphertext.txt has been encrypted
via AES-128 in ECB mode under the key given

Decrypt it. You know the key, after all.
"""
from Crypto.Cipher import AES
import binascii
def decrypt_aes(ciphertext, key):
    aes = AES.new(key, AES.MODE_ECB, 'ignored for ECB')
    plaintext = aes.decrypt(ciphertext)
    return plaintext

key = "YELLOW SUBMARINE"
filename = 'aes128_ciphertext.txt'
ciphertext = binascii.a2b_base64(''.join(line.strip() for line in open(filename)))
plaintext = decrypt_aes(ciphertext, key)
print plaintext