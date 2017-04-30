import os
import base64
import challenge9
import challenge10
import challenge11

SECRET = base64.decode("Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg\
aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq\
dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK")

# Key must be consistent (FIXED, do not change) but still random
KEY = generate_AES_key(16) # get random key

def rand_byte():
    return chr(random.randint(0,255))

def rand_bytes(amount):
    return ''.join([rand_byte() for i in range(amount)])

def generate_AES_key(amount):
    # generates 16 byte random key
    return rand_bytes(16)

def encryption_oracle(plaintext):

    message = plaintext + SECRET

    # pad message in case it isn't multiple of 16
    padder = challenge9.PKCS7Padder(block_size=16)
    plaintext = padder.pad(message)

    # EBC encrypt half the time, CBC encrypt half the time
    if bool(random.getrandbits(1)): # if 1 EBC encrypt
        ciphertext = challenge10.AES_ECB_encrypt(KEY, plaintext)
    else: # if 0 CBC encrypt
        # generate random IV
        iv = rand_bytes(16)
        ciphertext = challenge10.AES_CBC_encrypt(KEY, plaintext, iv)
    return ciphertext