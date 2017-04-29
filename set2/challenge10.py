'''
Implement CBC model:
CBC mode is a block cipher mode that allows us to encrypt irregularly-sized messages,
despite the fact that a block cipher natively only transforms individual blocks.

In CBC mode, each ciphertext block is added to the next plaintext
block before the next call to the cipher core.

The first plaintext block, which has no associated previous ciphertext block,
is added to a "fake 0th ciphertext block" called the initialization vector, or IV.

Implement CBC mode by hand by taking the ECB function you wrote earlier,
making it encrypt instead of decrypt (verify this by decrypting whatever
you encrypt to test), and using your XOR function from the previous exercise to combine them.

The file here is intelligible (somewhat) when CBC decrypted against
"YELLOW SUBMARINE" with an IV of all ASCII 0 (\x00\x00\x00 &c)
'''
from Crypto.Cipher import AES
import binascii

def xor_str(x, y):
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(x, y))

def AES_ECB_encrypt(key, plaintext):
    aes = AES.new(key, AES.MODE_ECB, 'ignored for ECB') # 3rd arg meaningless in ECB mode
    ciphertext = aes.encrypt(plaintext)
    return ciphertext

def AES_ECB_decrypt(ciphertext, key):
    aes = AES.new(key, AES.MODE_ECB, 'ignored for ECB')
    plaintext = aes.decrypt(ciphertext)
    return plaintext


def AES_CBC_encrypt(key, plaintext, iv):
    encoded = ""
    left = ""
    for i in range(0, len(plaintext), 16): # iterate blocks of 16
        right = plaintext[i:i+16]
        left = AES_ECB_encrypt(xor_str(left, right), key)
        encoded += left
    return encoded

def AES_CBC_decrypt(ciphertext, key, iv):
    decoded = ""
    left = iv
    for i in range(0, len(ciphertext), 16):
        decoded += xor_str(left, AES_ECB_decrypt(ciphertext[i: i + 16], key))
        left = ciphertext[i: i + 16]
    return decoded


# with open('data10.txt', 'r') as encoded_text:
    # data = encoded_text.read().decode('base64')

# print AES_CBC_decrypt(data, "YELLOW SUBMARINE", '\x00' * 16)
