filePath = "day6Puzzle1Sample.txt"
#filePath = "day6Puzzle1.txt"


class Coordinate:
    def __init__(self, rawLine):
        lineSplit = rawLine.strip().split(",")
        xValue = lineSplit[1].strip()
        yValue = lineSplit[0]

        self.xValue = int(xValue)
        self.yValue = int(yValue)
        self.label = xValue + "|" + yValue
        self.isInfinite = 0
        self.numberOfPoints = 0

class Helper:    
    def calculateDistance(self, xValue, yValue, coord):
        return abs(coord.xValue - xValue) + abs(coord.yValue - yValue)



class Main:
    def run(self):
        with open(filePath, 'r') as f:
            lines = f.readlines()

        xMin = 500
        yMin = 500
        xMax = 0
        yMax = 0
        coords = []
        for line in lines[:]:
            coord = Coordinate(line)
            if coord.xValue > xMax:
                xMax = coord.xValue
            if coord.xValue < xMin:
                xMin = coord.xValue
            if coord.yValue > yMax:
                yMax = coord.yValue
            if coord.yValue < yMin:
                yMin = coord.xValue
            coords.append(coord)
    
        helper = Helper()
        xCounter = xMin
        while xCounter <= xMax:
            yCounter = yMin
            while yCounter <= yMax:
                minDistance = 1000
                distanceConflict = False
                bestCoord = coords[0]
                for coord in coords[:]:
                    distance = helper.calculateDistance(xCounter, yCounter, coord)
                    if distance==minDistance:
                        distanceConflict = True
                    elif distance < minDistance:
                        distanceConflict = False
                        bestCoord = coord
                        minDistance = distance
                if not distanceConflict:
                    bestCoord.numberOfPoints+=1
                    if xCounter==xMin or xCounter==xMax or yCounter==yMin or yCounter==yMax:
                        bestCoord.isFinite = 1
                yCounter+=1
            xCounter+=1        

        coordCounter = len(coords)-1
        while coordCounter>=0:
            if coords[coordCounter].isInfinite:
                coords.pop(coordCounter)
            coordCounter = coordCounter - 1

        coords.sort(key=lambda item: (item.numberOfPoints), reverse=True)
        for coord in coords[:]:
            print(coord.label + " -> " + str(coord.numberOfPoints))

        print("Max number is " + str(coords[0].numberOfPoints) + ". Value is " + coords[0].label + ".")
Main().run()
    
