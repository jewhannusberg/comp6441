import os
import random
import challenge9 # for PKCS padding
import challenge10 # AES (ECB and CBC) encryption

def rand_byte():
    return chr(random.randint(0,255))

def rand_bytes(amount):
    return ''.join([rand_byte() for i in range(amount)])

def generate_AES_key(amount):
    # generates 16 byte random key
    return rand_bytes(16)

def encryption_oracle(plaintext):
    key = generate_AES_key(16) # get random key

    # append 5-10 bytes (random) before and 5-10 bytes after
    prefix = rand_bytes(random.randint(5,10))
    suffix = rand_bytes(random.randint(5,10))

    plaintext = prefix + plaintext + suffix

    # pad message in case it isn't multiple of 16
    padder = challenge9.PKCS7Padder(block_size=16)
    plaintext = padder.pad(plaintext)

    # EBC encrypt half the time, CBC encrypt half the time
    if bool(random.getrandbits(1)): # if 1 EBC encrypt
        ciphertext = challenge10.AES_ECB_encrypt(key, plaintext)
    else: # if 0 CBC encrypt
        # generate random IV
        iv = rand_bytes(16)
        ciphertext = challenge10.AES_CBC_encrypt(key, plaintext, iv)
    return ciphertext
"""
def detect_AES_encryption(ciphertext, block_size):
    # detect which encryption type. Return True for ECB and False for CBC
    num_blocks = len(ciphertext)/block_size
    # given hint, we assume that there is some repition of ciphertext
    # same plaintext always encodes to same ciphertext in AES ECB encryption
    # decrypt AES_ECB using challenge7
    for i in range(num_blocks): # loop through every 16 byte section of text
        for j in range(i+1, num_blocks): # loop through every other line
            if ciphertext[i*block_size:(i+1)*block_size] == ciphertext[j*block_size:(j+1)*block_size]:
                return True
    return False
"""
print encryption_oracle("testingblahblahs")