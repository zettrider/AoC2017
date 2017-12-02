import fileinput

puzzleInput = list(fileinput.input('02_input.txt'))

def getv1Checksum(sheetIn):
	checksumCounter = 0

	for item in range (0 ,len(sheetIn)):
		maxValue = max([int(i) for i in sheetIn[item].split()])
		minValue = min([int(i) for i in sheetIn[item].split()])
		checksumCounter += maxValue - minValue
	
	return(checksumCounter)

def getv2Checksum(sheetIn):
    checksumCounter = 0
    
    for item in puzzleInput:
        for x, y in [[int(a), int(b)] for a in item.split() for b in item.split()]:
            if x == y:
                continue
            elif x % y == 0:
                checksumCounter += (x // y)
            else:
                continue

    return(checksumCounter)

print(getv1Checksum(puzzleInput))
print(getv2Checksum(puzzleInput))