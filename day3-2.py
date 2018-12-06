#filePath = "day3Puzzle1Sample.txt"
filePath = "day3Puzzle1.txt"


class ClaimHelper:
    def checkForConflicts(self, claimName, claimStart, claimEnd, sourceList):
        claimList = sourceList[claimStart:claimEnd]
        isFirstClaim = claimStart == 0
        isLastClaim = claimEnd == len(sourceList)-1
        otherClaims = []
        if isFirstClaim:
            otherClaims = sourceList[claimEnd+1:]
        if isLastClaim:
            otherClaims = sourceList[:claimStart-1]
        if not isFirstClaim and not isLastClaim:
            otherClaims = sourceList[:claimStart-1] + sourceList[claimEnd+1:]
        
        isConflict = False
        for target in claimList[:]:
            if target in otherClaims:
                isConflict = True
                break
        if not isConflict:
            print("the answer is " + claimName)


class Main:
    def run(self):
        with open(filePath, 'r') as f:
            lines = f.readlines()

        plannedCoordinates = []
        for line in lines[:]:
            splitValues = line.split(" ")
            
            claim = splitValues[0]

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
                    plannedCoordinates.append(claim + "|" + str(locationX + xCounter) + "|" + str(locationY + yCounter))
                    xCounter+=1
                yCounter+=1

        plannedCoordinates.sort()

        claims = []
        listWithoutClaims = []
        listCounter = 0
        helper = ClaimHelper()
        while listCounter<len(plannedCoordinates):
            splitValue = plannedCoordinates[listCounter].split("|")
            claims.append(splitValue[0])
            listWithoutClaims.append(splitValue[1] + "|" + splitValue[2])
            listCounter+=1

        startOfClaim = 0
        listCounter = 0
        previousClaim = claims[0]
        while listCounter<len(claims):
            if previousClaim!=claims[listCounter]:        
                helper.checkForConflicts(previousClaim, startOfClaim, listCounter-1, listWithoutClaims)
                previousClaim = claims[listCounter]
                startOfClaim = listCounter
            listCounter+=1
        helper.checkForConflicts(previousClaim, startOfClaim, len(claims), listWithoutClaims)

Main().run()