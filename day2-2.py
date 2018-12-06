#filePath = "day2Puzzle2Sample.txt"
filePath = "day2Puzzle1.txt"
with open(filePath, 'r') as f:
    lines = f.readlines()

currentPosition = 0
for line in lines[:]:
    i = currentPosition
    while i < len(lines):
        j=0
        numberOfDiffs = 0
        while j < len(line):
            if (line[j]!=lines[i][j]):
                numberOfDiffs+=1
                if (numberOfDiffs>1):
                    j=99            
            j+=1
        if (numberOfDiffs == 1):
            print(line + " - " + lines[i])
            answer = []
            j=0
            while j < len(line):
                if (line[j]==lines[i][j]):
                    answer.append(line[j])
                j+=1
            print(''.join(answer))
        i += 1
    currentPosition+=1

