import os
import random

def _generate_AES_key(amount):
    # generates 16 byte random key
    return os.urandom(16)

def encryption_oracle(plaintext):
    key = _generate_AES_key(16) # get random key

    # append 5-10 bytes (random) before and 5-10 bytes after
    prefix = _generate_AES_key(random.randint(5,10))
    suffix = _generate_AES_key(random.randint(5,10))

    plaintext = prefix + plaintext + suffix

    # EBC encrypt half the time

    # CBC encrypt half the time

    # detect which encryption type

print encryption_oracle("testing")