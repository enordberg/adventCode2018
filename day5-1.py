#filePath = "day5Puzzle1Sample.txt"
filePath = "day5Puzzle1.txt"


class Main:
    def run(self):
        with open(filePath, 'r') as f:
            lines = f.readlines()
    
        sourceText = lines[0];

        changesMade = True
        while changesMade:
            changesMade = False
            counter = 0
            while not changesMade and counter < len(sourceText)-1:
                if sourceText[counter]!=sourceText[counter+1] and sourceText[counter].lower() == sourceText[counter+1].lower():
                    sourceText = sourceText.replace(sourceText[counter] + sourceText[counter+1], "")
                    changesMade = True
                counter+=1
        
        print("Resulting string = " + sourceText)
        print("Length = " + str(len(sourceText)))

Main().run()
    
