import string

#filePath = "day7Puzzle1Sample.txt"
#baseTimeAdd = 0
#numberOfWorkers = 2
filePath = "day7Puzzle1.txt"
baseTimeAdd = 60
numberOfWorkers = 5

def calculateTimeForLetter(letter):
    if letter == "A":
        letterCount = 0
    if letter == "B":
        letterCount = 1
    if letter == "C":
        letterCount = 2
    if letter == "D":
        letterCount = 3
    if letter == "E":
        letterCount = 4
    if letter == "F":
        letterCount = 5
    if letter == "G":
        letterCount = 6
    if letter == "H":
        letterCount = 7
    if letter == "I":
        letterCount = 8
    if letter == "J":
        letterCount = 9
    if letter == "K":
        letterCount = 10
    if letter == "L":
        letterCount = 11
    if letter == "M":
        letterCount = 12
    if letter == "N":
        letterCount = 13
    if letter == "O":
        letterCount = 14
    if letter == "P":
        letterCount = 15
    if letter == "Q":
        letterCount = 16
    if letter == "R":
        letterCount = 17
    if letter == "S":
        letterCount = 18
    if letter == "T":
        letterCount = 19
    if letter == "U":
        letterCount = 20
    if letter == "V":
        letterCount = 21
    if letter == "W":
        letterCount = 22
    if letter == "X":
        letterCount = 23
    if letter == "Y":
        letterCount = 24
    if letter == "Z":
        letterCount = 25
    return letterCount + 1 + baseTimeAdd

class Step:
    def __init__(self, name):
        self.stepName = name
        self.stepNeeds = []
        self.stepEnables = []
        self.timeRequired = calculateTimeForLetter(name)

    def addNeed(self, need):
        if not need in self.stepNeeds:
            self.stepNeeds.append(need)

    def addEnables(self, enables):
        if not enables in self.stepEnables:
            self.stepEnables.append(enables)

    def printStep(self):
        print(self.stepName + " Needs: " + ''.join(str(need) for need in self.stepNeeds) + "; Enables: " + ''.join(str(enable) for enable in self.stepEnables))

class ActiveTime:
    def __init__(self, letter, time):
        self.letter = letter
        self.time = time

class StepItems:
    def __init__(self):
        self.steps = {} 
        self.ready = []
        self.completedSteps = []

    def addItem(self, rawInput):
        inputSplit = rawInput.split(",")
        needs = str(inputSplit[0])
        enables = str(inputSplit[1]).strip()

        if needs in self.steps:
            self.steps[needs].addEnables(enables)
        else:
            step = Step(needs)
            step.addEnables(enables)
            self.steps[needs] = step
        
        if enables in self.steps:
            self.steps[enables].addNeed(needs)
        else:
            step = Step(enables)
            step.addNeed(needs)
            self.steps[enables] = step

    def findReadyItems(self):
        self.ready = []
        for key, value in self.steps.items():
            if len(value.stepNeeds) == 0:
                self.ready.append(value)
        self.ready.sort(key = lambda x: x.stepName)
    
    def processStep(self, stepName):        
        step = self.steps[stepName]
        for enabledStepName in step.stepEnables[:]:
            enabledStep = self.steps[enabledStepName]
            if stepName in enabledStep.stepNeeds:
                enabledStep.stepNeeds.remove(stepName)
            if len(enabledStep.stepNeeds)==0:
                self.ready.append(enabledStep)
        self.completedSteps.append(stepName)
        self.ready.sort(key = lambda x: x.stepName)    


class Main:    
    def run(self):
        with open(filePath, 'r') as f:
            lines = f.readlines()

        items = StepItems()
        
        for line in lines[:]:
            items.addItem(line)
        
        #for key, value in items.steps.items():
            #value.printStep()

        items.findReadyItems()

        currentNumberOfWorkers = numberOfWorkers
        activeTimes = []

        previousTime = 0
        while len(items.ready)>0 or len(activeTimes)>0:            
            if len(activeTimes)>0:
                activeTimes.sort(key=lambda x: x.time)
                previousTime = activeTimes[0].time
                while len(activeTimes)>0 and activeTimes[0].time == previousTime:
                    active = activeTimes.pop(0)
                    items.processStep(active.letter)
                    #print(active.letter + " -> " + str(active.time))
                    currentNumberOfWorkers+=1
            stepsForCurrentTime = []
            while currentNumberOfWorkers>0 and len(items.ready)>0:                
                item = items.ready.pop(0)
                if not item in items.completedSteps:                    
                    stepsForCurrentTime.append(item)
                    currentNumberOfWorkers = currentNumberOfWorkers - 1
            for step in stepsForCurrentTime[:]:
                activeTimes.append(ActiveTime(step.stepName, step.timeRequired+previousTime))    
                #print("active " + step.stepName + " -> " + str(step.timeRequired+previousTime))       
        
        print("Step order = " + ''.join(str(item) for item in items.completedSteps))
        print("Time = " + str(previousTime))
Main().run()
    
