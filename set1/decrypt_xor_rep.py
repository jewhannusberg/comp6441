"""
challenge6_data.txt has been encrypted with repeating key XOR
need to break it by finding the key and decrypting

It's been base64'd after being encrypted with repeating-key XOR

"""
import binascii
import base64
import numpy
import xor_cipher # single character xor cipher decrypt
import frequencies
import rep_key_xor # decrypt repeating key xor

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

# break the ciphertext into blocks of KEYSIZE length.
def block_ciphertext(data, k):
    start = 0
    return [data[i:i+k] for i in range(0, len(data), k)]

def transpose(blocks, k):
    transposed = []
    for i in range(0, k):
        transposed.append([block[i:i+1] for index, block in enumerate(blocks)])
    return transposed

def decrypt_repeated_key_xor(data):
    def _decrypt():
        return None
    distances = []
    for keylen in range(MIN_KEYSIZE, MAX_KEYSIZE+1):
        pair = block_ciphertext(data, keylen)[0:N]
        dist = hamming_dist(pair[0], pair[1])
        normalised_dist = dist/keylen
        distances.append((keylen, normalised_dist))
    # sort distances by hamming_dist
    distances = sorted(distances, key=lambda dist: dist[1])

    for dist in distances:
        keylen = dist[0]
        cipher_key = []

        # transpose all the blocks
        ciphertext_blocks = block_ciphertext(data, keylen)
        transposed_blocks = transpose(ciphertext_blocks, keylen)

        # break as if single character XOR to get each char of the key string
        for block in transposed_blocks:
            cipher_key.append(xor_cipher.decode_xor(reduce(lambda a,b: a+b, block))[1])

        # show all the possible key strings for each keysize length, sorted lowest to highest hamming distances
        max_key_score = 0
        if len(''.join(cipher_key)) > 1 and frequencies.score(''.join(cipher_key)) > max_key_score:
            max_key_score = frequencies.score(''.join(cipher_key))
            key = ''.join(cipher_key)

    print key
    # rep_key_xor.encrypt(data, key)


# read file data
with open('challenge6_data.txt', 'r') as rf:
    decoded = base64.b64decode(rf.read())
decrypt_repeated_key_xor(decoded)