#filePath = "day6Puzzle1Sample.txt"
#minSize = 32
filePath = "day6Puzzle1.txt"
minSize = 10000


class Coordinate:
    def __init__(self, rawLine):
        lineSplit = rawLine.strip().split(",")
        xValue = lineSplit[1].strip()
        yValue = lineSplit[0]

        self.xValue = int(xValue)
        self.yValue = int(yValue)
        self.label = xValue + "|" + yValue

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
        numberOfGoodPoints = 0
        while xCounter <= xMax:
            yCounter = yMin
            while yCounter <= yMax:
                totalDistance = 0
                for coord in coords[:]:
                    totalDistance = totalDistance + helper.calculateDistance(xCounter, yCounter, coord)                    
                if totalDistance<minSize:
                    numberOfGoodPoints += 1
                yCounter+=1
            xCounter+=1        

        print("Region size is " + str(numberOfGoodPoints) + ".")
Main().run()
    
