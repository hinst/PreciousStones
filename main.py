import sys

def getLongestSequenceLength(text):
    longestSequenceLength = 0
    currentSequenceLength = 0
    lastCharacter = ' '
    for character in text:
        if character != lastCharacter:
            currentSequenceLength = 0
        currentSequenceLength += 1
        if longestSequenceLength < currentSequenceLength:
            longestSequenceLength = currentSequenceLength
        lastCharacter = character
    return longestSequenceLength

inputFile = sys.stdin
if len(sys.argv) > 1:
    inputFile = open(sys.argv[1], 'r')
lines = inputFile.readlines()
size = int(lines[0].strip())
for line in lines[1:]:
    line = line.strip()

