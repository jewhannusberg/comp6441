# read hex encoded data
import binascii
from decrypt_aes128ecb import decrypt_aes

def is_AES_ECB(ciphertext, block_size):
    num_blocks = len(ciphertext)/block_size
    # given hint, we assume that there is some repition of ciphertext
    # same plaintext always encodes to same ciphertext in AES ECB encryption
    # decrypt AES_ECB using challenge7
    for i in range(num_blocks): # loop through every 16 byte section of text
        for j in range(i+1, num_blocks): # loop through every other line
            if ciphertext[i*block_size:(i+1)*block_size] == ciphertext[j*block_size:(j+1)*block_size]:
                return True
    return False

fname = 'aes_detection.txt'
for line in open(fname, 'r'):
    line = line.strip()
    line = binascii.a2b_hex(line)
    if is_AES_ECB(line, 16):
        print binascii.b2a_hex(line)