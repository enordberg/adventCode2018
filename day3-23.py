#filePath = "day3Puzzle1Sample.txt"
filePath = "day3Puzzle.txt"

class Claim:
    def __init__(self, rawInput):
        splitValues = rawInput.split(" ")
        
        self.claim = splitValues[0]

        location = splitValues[2]
        location = location.replace(":", "")
        locationSplit = location.split(",")
        self.locationX = int(locationSplit[0])
        self.locationY = int(locationSplit[1])
        #print("loc x + " + str(locationX))
        #print("loc y + " + str(locationY))

        size = splitValues[3]
        sizeSplit = size.split("x")
        self.sizeX = int(sizeSplit[0])
        self.sizeY = int(sizeSplit[1])

        yCounter = 0
        self.plannedCoordinates = []
        while yCounter<self.sizeY:
            xCounter = 0
            while xCounter<self.sizeX:            
                self.plannedCoordinates.append(str(self.locationX + xCounter) + "|" + str(self.locationY + yCounter))
                xCounter+=1
            yCounter+=1

        self.hasConflicts = False

    def compareForConflicts(self, otherClaim):
        for coord in self.plannedCoordinates:
            if coord in otherClaim.plannedCoordinates:
                self.hasConflicts = True
                otherClaim.hasConflcits = True
                break


class Main:
    def run(self):
        with open(filePath, 'r') as f:
            lines = f.readlines()
    
        claims = []
        for line in lines[:]:
            claims.append(Claim(line))
        
        i = 0
        while i<len(claims):            
            if not claims[i].hasConflicts:
                j = 0
                while j<len(claims):
                    if not claims[j].hasConflicts and i!=j:
                        claims[i].compareForConflicts(claims[j])
                    j+=1
            i+=1

        i = 0
        while i<len(claims):            
            if not claims[i].hasConflicts:
                j = 0
                while j<len(claims):
                    if i!=j:
                        claims[i].compareForConflicts(claims[j])
                    j+=1
            i+=1
                
        i = 0
        while i<len(claims):            
            if not claims[i].hasConflicts:
                print("winner " + claims[i].claim)
            i+=1    
Main().run()