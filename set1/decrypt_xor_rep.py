"""
challenge6_data.txt has been encrypted with repeating key XOR
need to break it by finding the key and decrypting

It's been base64'd after being encrypted with repeating-key XOR

"""
import binascii
import base64
import numpy


MIN_KEYSIZE = 2 # initial guess of key length
MAX_KEYSIZE = 40
N = 2 # number of likely keys (random, can try other values)

def hamming_dist(actual, guess):
    # calculate hamming distance between two byte arrays
    actual = bytearray(actual)
    guess = bytearray(guess)
    
    if len(actual) != len(guess):
        raise ValueError("Hamming distance undefined for unequal length strings")
    else:
        dist = 0
        for i in range(len(guess)):
            if guess[i] != actual[i]:
                dist += bin(guess[i] ^ actual[i]).count("1")
    return dist
# def block_ciphertext(data, keylen):

def decrypt_repeated_key_xor(data):
    def _decrypt(keylen):
        key_dist = hamming_dist(data[0:keylen], data[keylen:2*keylen])
        key_dist_norm = key_dist/keylen
        return key_dist_norm

    keylen = MIN_KEYSIZE

    key_results = []
    probable_keys = []    
    for keylen in range(MIN_KEYSIZE, MAX_KEYSIZE):
        result = _decrypt(keylen)
        key_results.append(result)
    key_results = numpy.asarray(key_results)

    probable_keys = list(key_results.argsort()[:N]) # 2 smallest hamming dist indices




# read file data
with open('challenge6_data.txt', 'r') as rf:
    decoded = base64.b64decode(rf.read())
decrypt_repeated_key_xor(decoded)