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
        self.isInfinite = -1

class Helper:
    def __init__(self, xMin, xMax, yMin, yMax):
        self.xMin = xMin
        self.xMax = xMax        
        self.yMin = yMin
        self.yMax = yMax

    def createLabel(self, xValue, yValue):
        return str(xValue) + "|" + str(yValue)
    
    def calculateValue(self, xValue, yValue, positions, lastRoundOfChanges):
        if xValue<self.xMin or xValue>self.xMax or yValue<self.yMin or yValue>self.yMax:
            return ""
        position = self.createLabel(xValue, yValue)
        if position in lastRoundOfChanges:
            return ""
        if positions[position]!="":
            return positions[position]
        return ""

    def calculateValueBasedOnNeighbors(self, xValue, yValue, positions, lastRoundOfChanges):
        currentValue = self.calculateValue(xValue, yValue, positions, [])
        if currentValue!="":
            return currentValue
        possibleValues = []
        left = self.calculateValue(xValue-1, yValue, positions, lastRoundOfChanges)
        if left!="":            
            possibleValues.append(left)
        top = self.calculateValue(xValue, yValue-1, positions, lastRoundOfChanges)
        if top!="" and top not in possibleValues:
            possibleValues.append(top)
        right = self.calculateValue(xValue+1, yValue, positions, lastRoundOfChanges)
        if right!="" and right not in possibleValues:
            possibleValues.append(right)
        bottom = self.calculateValue(xValue, yValue+1, positions, lastRoundOfChanges)
        if bottom!="" and bottom not in possibleValues:
            possibleValues.append(bottom)    
        if len(possibleValues)==0:
            del possibleValues
            return ""
        elif len(possibleValues)==1:
            result = possibleValues[0]            
        else:
            result = "~"        
        del possibleValues            
        return result
        

    def subLetter(self, label):
        if label=="1|1":
            return "a"
        if label=="6|1":
            return "b"
        if label=="3|8":
            return "c"
        if label=="4|3":
            return "d"
        if label=="5|5":
            return "e"
        if label=="9|8":
            return "f"
        return "."


class Main:
    def run(self):
        with open(filePath, 'r') as f:
            lines = f.readlines()

        xMin = 500
        yMin = 500
        xMax = 0
        yMax = 0
        positions = {}
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
            positions[coord.label] = coord.label
        xMin = xMin -1
        xMax = xMax + 1
        yMin = yMin - 1
        yMax = yMax + 1
        
        del lines

        helper = Helper(xMin, xMax, yMin, yMax)
        xCounter = xMin
        while xCounter <= xMax:
            yCounter = yMin
            while yCounter <= yMax:
                label = helper.createLabel(xCounter, yCounter)                   
                if not label in positions:             
                    positions[label] = ""                                            
                yCounter+=1
            xCounter+=1   

        infiniteCoords = []        
        changesMade = True
        lastRoundOfChanges = []
        while changesMade:
            del lastRoundOfChanges
            lastRoundOfChanges = []
            changesMade = False
            xCounter = xMin
            while xCounter <= xMax:
                yCounter = yMin
                while yCounter <= yMax:
                    label = helper.createLabel(xCounter, yCounter)
                    oldValue = helper.calculateValue(xCounter, yCounter, positions, [])
                    newValue = helper.calculateValueBasedOnNeighbors(xCounter, yCounter, positions, lastRoundOfChanges)
                    if oldValue != newValue:
                        changesMade = True                        
                        positions[label] = newValue                        
                        lastRoundOfChanges.append(label)
                        if newValue!="" and (xCounter == xMin or xCounter == xMax or yCounter == yMin or yCounter == yMax):
                            if not label in infiniteCoords:
                                infiniteCoords.append(newValue)                        
                    yCounter+=1
                xCounter+=1        

        # xCounter = xMin
        # while xCounter <= xMax:
        #     yCounter = yMin
        #     xRow = []
        #     while yCounter <= yMax:
        #         label = helper.createLabel(xCounter, yCounter)        
        #         if label not in positions:
        #             xRow.append("-")
        #         else:                                                    
        #             letter = helper.subLetter(positions[label])
        #             xRow.append(letter)                                    
        #         yCounter+=1
        #     print(''.join(str(x) for x in xRow))
        #     xCounter+=1     


        allValues = []
        for key in positions.keys():
            value = positions[key]
            if value!="" and value!="~" and not value in infiniteCoords:
                allValues.append(positions[key])
        allValues.sort()

        maxNumber = 0
        maxValue = ""
        currentNumber = 0
        previousValue = ""
        for value in allValues[:]:
            if value != previousValue:
                if currentNumber > maxNumber:
                    maxNumber = currentNumber
                    maxValue = previousValue
                previousValue = value
                currentNumber = 0
            currentNumber+=1
        if currentNumber > maxNumber:
            maxNumber = currentNumber
            maxValue = previousValue

        print("Max number is " + str(maxNumber) + ". Value is " + maxValue + ".")
Main().run()
    
