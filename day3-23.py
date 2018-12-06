#filePath = "day3Puzzle1Sample.txt"
filePath = "day3Puzzle1.txt"

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
        self.hasConflicts = False

    def compareForConflicts(self, otherClaim):
        if not (self.locationX > otherClaim.locationX + otherClaim.sizeX-1 or otherClaim.locationX > self.locationX + self.sizeX-1 or self.locationY > otherClaim.locationY + otherClaim.sizeY-1 or otherClaim.locationY > self.locationY + self.sizeY-1):
            self.hasConflicts = True
            otherClaim.hasConflcits = True


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