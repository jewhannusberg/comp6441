'''
Brute forece for Caeser cipher
'''
import string

KEY = 'abcdefghijklmnopqrstuvwxyz'
UPPER_KEY = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def decrypt(n, ciphertext):
    """Decrypt the string and return the plaintext"""
    result = ''

    for l in ciphertext:
        if l.islower():
            i = (KEY.index(l) - n) % 26
            result += KEY[i]
        elif l.isupper():
            i = (UPPER_KEY.index(l) - n) % 26
            result += UPPER_KEY[i]
        else:
            result += l
    return result

ciphertext = "iodj{EuxwhIrufhLvEhvwIrufh}"

print decrypt(3, ciphertext)