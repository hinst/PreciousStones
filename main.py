import sys

inputFile = sys.stdin
if len(sys.argv) > 1:
    inputFile = open(sys.argv[1], 'r')
lines = inputFile.readlines()
size = int(lines[0].strip())
print(size)
for line in lines[1:]:
    line = line.strip()
    print(line)
