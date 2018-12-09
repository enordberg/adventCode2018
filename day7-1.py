#filePath = "day7Puzzle1Sample.txt"
filePath = "day7Puzzle1.txt"


class Step:
    def __init__(self, name):
        self.stepName = name
        self.stepNeeds = []
        self.stepEnables = []

    def addNeed(self, need):
        if not need in self.stepNeeds:
            self.stepNeeds.append(need)

    def addEnables(self, enables):
        if not enables in self.stepEnables:
            self.stepEnables.append(enables)

    def printStep(self):
        print(self.stepName + " Needs: " + ''.join(str(need) for need in self.stepNeeds) + "; Enables: " + ''.join(str(enable) for enable in self.stepEnables))

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
                self.ready.append(value.stepName)
        self.ready.sort()
    
    def processStep(self, stepName):        
        step = self.steps[stepName]
        for enabledStepName in step.stepEnables[:]:
            enabledStep = self.steps[enabledStepName]
            if stepName in enabledStep.stepNeeds:
                enabledStep.stepNeeds.remove(stepName)
            if len(enabledStep.stepNeeds)==0:
                self.ready.append(enabledStepName)        
        self.completedSteps.append(stepName)
        self.ready.sort()
        #print('-'.join(str(name) for name in self.ready))


class Main:
    def run(self):
        with open(filePath, 'r') as f:
            lines = f.readlines()

        items = StepItems()
        
        for line in lines[:]:
            items.addItem(line)
        
        # for key, value in items.steps.items():
        #     value.printStep()

        items.findReadyItems()

        while len(items.ready)>0:
            item = items.ready.pop(0)
            if not item in items.completedSteps:
                items.processStep(item)
        
        print("Step order = " + ''.join(str(item) for item in items.completedSteps))
Main().run()
    
