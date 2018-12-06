#filePath = "day3Puzzle1Sample.txt"
filePath = "day3Puzzle2.txt"


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

        print("array gathered")
        plannedCoordinates.sort()
        print("array sorted")

        claims = []
        listWithoutClaims = []
        badClaims = []
        listCounter = 0
        while listCounter<len(plannedCoordinates):
            splitValue = plannedCoordinates[listCounter].split("|")
            claimValue = splitValue[0]
            coordValue = splitValue[1] + "|" + splitValue[2]
            if coordValue in listWithoutClaims:
                claimIndex = listWithoutClaims.index(coordValue)
                badClaim = claims[claimIndex]
                if not claimValue in badClaims:
                    badClaims.append(claimValue)
                if not badClaim in badClaims:
                    badClaims.append(badClaim)
            else:
                claims.append(claimValue)                
                listWithoutClaims.append(coordValue)
            listCounter+=1
        print("dupe scan complete")

        for possibleClaim in claims:
            if not possibleClaim in badClaims:
                print("The answer is " + possibleClaim)

Main().run()