from xor_cipher import decode_xor

res = []
with open('data.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        res.append(decode_xor(line))


# print max(res, key=lambda x: x[0])


for result in res:
    print result