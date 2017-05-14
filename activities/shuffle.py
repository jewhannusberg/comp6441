import re

fname = open("shuffled_text.txt", "rw+")

lines = fname.readlines()
new_lines = [0] * 700
ctr = 0

for i in range(594):
  for line in lines:
    match = re.match(r'.*(:::*:*(\d+):+).*', line, re.M|re.I)
    with_cols = match.group(1)

    line_no = int(match.group(2))

    if line_no == i:
      line = line.replace(with_cols,'')
      # new_lines.insert(line_no, line)
      new_lines.append(line)

new_lines = [item for item in new_lines if item != 0]
# print new_lines
new_file = open('reordered_text.txt', 'w')
for item in new_lines:
  new_file.write(item)
for item in new_lines:
    print item