"""
hex string has been XORd against a single character

find the key and decrypt the message
"""

import binascii

def _score(s):
    # get all alphabetic characters from each decoded string
    letters = filter(lambda x: 'a'<=x<='z' or 'A'<=x<='Z', s) 
    # return a value of how many alphabetic characters in each decoded string
    return float(len(letters)) / len(s)


def decode_xor(hex_str):
    encoded = binascii.unhexlify(hex_str)

    res = []
    # loop through number of hex characters
    for xor_key in range(256):
        # decode each byte
        decoded = ''.join(chr(ord(x) ^ xor_key) for x in encoded)
        # create a list of all decoded values
        res.append([_score(decoded), ''.join(decoded)])

    # pick only first value of result list
    return max(res, key=lambda x: x[0])

# xord_str = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

# output = decode_xor(xord_str)