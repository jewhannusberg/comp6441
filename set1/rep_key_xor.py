"""
XOR Encryption with repeating key

Input:
Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal

Key: ICE

Output:
0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
"""

import binascii

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return '%x' % (int(a[:len(b)],16)^int(b,16))
    else:
        return '%x' % (int(a,16)^int(b[:len(a)],16))

# text = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
# print text
# key = "ICE"

# convert every byte of text to hex component
def encrypt(text, key):
    hex_text = binascii.hexlify(text)

    len_text = len(hex_text)
    len_key = len(key)
    try:
        repetitions = len_text/len_key
    except:
        print "not even number of repetitions, need to chop word"

    tot_key = key * repetitions
    hex_key = binascii.hexlify(tot_key)

    xor_text = strxor(hex_text, hex_key)
    print xor_text
