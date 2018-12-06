#filePath = "day3Puzzle1Sample.txt"
filePath = "day3Puzzle1.txt"
with open(filePath, 'r') as f:
    lines = f.readlines()

plannedCoordinates = []
for line in lines[:]:
    splitValues = line.split(" ")
        
    location = splitValues[2]
    location = location.replace(":", "")
    locationSplit = location.split(",")
    locationX = int(locationSplit[0])
    locationY = int(locationSplit[1])
    #print("loc x + " + str(locationX))
    #print("loc y + " + str(locationY))

    size = splitValues[3]
    sizeSplit = size.split("x")
    sizeX = int(sizeSplit[0])
    sizeY = int(sizeSplit[1])
    #print("size x + " + str(sizeX))
    #print("size y + " + str(sizeY))

    yCounter = 0
    while yCounter<sizeY:
        xCounter = 0
        while xCounter<sizeX:
            
            plannedCoordinates.append(str(locationX + xCounter) + "|" + str(locationY + yCounter))
            xCounter+=1
        yCounter+=1

plannedCoordinates.sort()
numberOfRepeats = 0
planCounter = 0;
previousValue = ""
isRepeating = False
while planCounter<len(plannedCoordinates):
    if plannedCoordinates[planCounter] == previousValue:
        if not isRepeating:
            numberOfRepeats+=1
            isRepeating = True
    else:
        isRepeating = False            
    previousValue = plannedCoordinates[planCounter]
    planCounter+=1
print("number of repeats = " + str(numberOfRepeats))
#print(plannedCoordinates)

