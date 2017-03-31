"""
Write a function that takes two equal-length buffers and produces their XOR combination.

If your function works properly, then when you feed it the string:

Hex -> Binary -> XOR -> Hex

XOR rules:
0 xor 0 = 0
0 xor 1 = 1
1 xor 0 = 1
1 xor 1 = 0
"""

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return '%x' % (int(a[:len(b)],16)^int(b,16))
    else:
        return '%x' % (int(a,16)^int(b[:len(a)],16))

# str1 = "1c0111001f010100061a024b53535009181c"

# str2 = "686974207468652062756c6c277320657965"

# print strxor(str1, str2)
