import sys

def getLongestSequenceLength(text):
    longestSequenceLength = 0
    currentSequenceLength = 0
    lastCharacter = ' '
    textLength = len(text)
    for i in range(textLength * 2):
        character = text[i % textLength]
        if character != lastCharacter:
            currentSequenceLength = 0
        currentSequenceLength += 1
        if longestSequenceLength < currentSequenceLength:
            longestSequenceLength = currentSequenceLength
        lastCharacter = character
    return longestSequenceLength

def mutateText(text, index):
    character = text[index]
    if character == "R":
        text[index] = "A"
    else:
        text[index] = "R"
    return text

def getMinBeauty(text):
    for i in range(text):
        mutatedText = mutateText(text, i)

inputFile = sys.stdin
if len(sys.argv) > 1:
    inputFile = open(sys.argv[1], 'r')
lines = inputFile.readlines()
size = int(lines[0].strip())
for line in lines[1:]:
    line = line.strip()
    longestSequenceLength = getLongestSequenceLength(line)
    print(longestSequenceLength)

