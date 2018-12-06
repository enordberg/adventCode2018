from datetime import datetime

#filePath = "day4Puzzle1Sample.txt"
filePath = "day4Puzzle1.txt"

class RawInputLine:
    def __init__(self, rawInput):
        rawInput = rawInput.replace("[", "")
        rawInputSplit = rawInput.split("]")
        rawDate = rawInputSplit[0]    
        self.eventDate = datetime.strptime(rawDate, '%Y-%m-%d %H:%M')

        rawText = rawInputSplit[1].strip()
        self.isWakesUp = rawText == "wakes up"
        self.isFallsAsleep = rawText == "falls asleep"
        if not self.isWakesUp and not self.isFallsAsleep:
            self.guardNumber = int(rawText.replace("Guard #", "").replace(" begins shift", ""))
        else:
            self.guardNumber = -1

class Guard:
    def __init__(self, guardNumber):
        self.guardNumber = guardNumber
        self.events = []
        self.totalSleepTime = -1
        self.mostCommonMinuteSleeping = -1
        self.numberOfMinutesForMostCommon = -1
    
    def determineNumberOfMinutesAsleep(self):
        self.totalSleepTime = -1
        sleepingAggregated = 0        
        isSleeping = False
        for event in self.events[:]:
            if event.isWakesUp and not isSleeping:
                print("error - wake up before sleeping")
                break
            if event.isFallsAsleep and isSleeping:
                print("error - falls asleep when sleeping")
                break
            if not event.isWakesUp and not event.isFallsAsleep and isSleeping:
                print("error - starting shift while sleeping")
                break
            if event.isFallsAsleep:
                isSleeping = True
                sleepingDate = event.eventDate
            if event.isWakesUp:
                isSleeping = False
                sleeptime = event.eventDate.minute - sleepingDate.minute # assumes same hour of day
                sleepingAggregated = sleepingAggregated + sleeptime
        if isSleeping:
            self.totalSleepTime = -1
            print("error - ended records while sleeping")
        else:
            self.totalSleepTime = sleepingAggregated
    
    def determineMostCommonMinuteSleeping(self):
        self.mostCommonMinuteSleeping = -1
        self.numberOfMinutesForMostCommon = -1
        sleepMinutes = []
        isSleeping = False
        for event in self.events[:]:
            if event.isWakesUp and not isSleeping:
                print("error - wake up before sleeping")
                break
            if event.isFallsAsleep and isSleeping:
                print("error - falls asleep when sleeping")
                break
            if not event.isWakesUp and not event.isFallsAsleep and isSleeping:
                print("error - starting shift while sleeping")
                break
            if event.isFallsAsleep:
                isSleeping = True
                sleepingDate = event.eventDate
            if event.isWakesUp:
                isSleeping = False
                for minute in range(sleepingDate.minute, event.eventDate.minute):
                    sleepMinutes.append(minute)
                
        if isSleeping:
            self.mostCommonMinuteSleeping = -1
            self.numberOfMinutesForMostCommon = -1
            print("error - ended records while sleeping")
        else:
            sleepMinutes.sort()
            previousMinute = -1
            currentOccurences = 0
            maxOccurences = -1
            maxOccurenceValue = -1            
            for minute in sleepMinutes[:]:
                if minute != previousMinute:
                    if currentOccurences > maxOccurences:
                        maxOccurences = currentOccurences
                        maxOccurenceValue = previousMinute
                    previousMinute = minute
                    currentOccurences = 0
                currentOccurences+=1
            if currentOccurences > maxOccurences:
                    maxOccurences = currentOccurences
                    maxOccurenceValue = previousMinute
            self.mostCommonMinuteSleeping = maxOccurenceValue
            self.numberOfMinutesForMostCommon = maxOccurences

class Main:
    def run(self):
        with open(filePath, 'r') as f:
            lines = f.readlines()
    
        events = []
        for line in lines[:]:
            events.append(RawInputLine(line))
        
        events.sort(key=lambda item: (item.eventDate))

        currentGuardNumber = -1
        for event in events[:]:
            if event.guardNumber == -1:
                event.guardNumber = currentGuardNumber
            else:
                currentGuardNumber = event.guardNumber
        if events[0].guardNumber == -1:
            print("first event has no guard number")

        events.sort(key=lambda item: (item.guardNumber, item.eventDate))
        guards = []
        
        previousGuard = -1        
        for event in events[:]:
            if event.guardNumber != previousGuard:
                if previousGuard!=-1:
                    guards.append(guard)
                guard = Guard(event.guardNumber)                
                previousGuard = event.guardNumber
            guard.events.append(event)

        for guard in guards[:]:
            guard.determineNumberOfMinutesAsleep()
        
        guards.sort(key=lambda item: (item.totalSleepTime), reverse=True)

        guards[0].determineMostCommonMinuteSleeping()
        worstGuard = guards[0]
        print("Guard #" + str(worstGuard.guardNumber) + ": Total sleep time=" + str(worstGuard.totalSleepTime) + " minutes.  Most common minute=" + str(worstGuard.mostCommonMinuteSleeping) + ".")
        print("Answer = " + str(worstGuard.guardNumber * worstGuard.mostCommonMinuteSleeping))

Main().run()
    
