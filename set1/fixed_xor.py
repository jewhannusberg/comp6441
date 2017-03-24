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

def hex_binary(hex_str):
    x = bin(int(str(hex_str), 16))[2:]
    bin_str = '0'*(8-len(x)%8) + x
    return bin_str


def _xor(str1, str2):
    out_str = int(str1, 2)^int(str2,2)
    out_str = bin(out_str)[2:].zfill(len(str1))
    return out_str

str1 = "1c0111001f010100061a024b53535009181c"

str2 = "686974207468652062756c6c277320657965"

bin_str1 = hex_binary(str1)

bin_str2 = hex_binary(str2)

xor_out = _xor(bin_str1, bin_str2)
print xor_out
hex_out = hex(int(xor_out, 2))
print hex_out