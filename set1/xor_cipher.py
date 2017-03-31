"""
hex string has been XORd against a single character

find the key and decrypt the message
"""

import binascii

def score_plaintext(s):
    # get all alphabetic characters from each decoded string
    letters = filter(lambda x: 'a'<=x<='z' or 'A'<=x<='Z', s) 
    # return a value of how many alphabetic characters in each decoded string
    return float(len(letters)) / len(s)

xord_str = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

encoded = binascii.unhexlify(xord_str)

res = []
# loop through number of hex characters
for xor_key in range(256):
    # decode each byte
    decoded = ''.join(chr(ord(x) ^ xor_key) for x in encoded)
    # create a list of all decoded values
    res.append([score_plaintext(decoded), ''.join(decoded)])

# pick only first value of result list
print max(res, key=lambda x: x[0])

