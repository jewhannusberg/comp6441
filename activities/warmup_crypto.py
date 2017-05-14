ciphertext= "TGPRGWTADEKI HI3OYNODONAT ES4LOCIINTB} FC4LURSDTHO_ LO1IRYAEEIU_ AM{NOPBAVNT_"

# Clearly a transposition-style cipher

ciphertext_words = ciphertext.split(' ')

plaintext = ""


for inner_index in range(len(ciphertext_words[0])):
    for index in range(len(ciphertext_words)):
        plaintext += ciphertext_words[index][inner_index]

print plaintext
