import string

#filePath = "day5Puzzle1Sample.txt"
filePath = "day5Puzzle1.txt"


class Main:
    def run(self):
        with open(filePath, 'r') as f:
            lines = f.readlines()
    
        sourceText = lines[0];
        alphas = []
        for letter in string.ascii_lowercase[:26]:
            alphas.append(sourceText.replace(letter, "").replace(letter.upper(), ""))

        alphaCounter = 0
        while alphaCounter < len(alphas):  
            alpha = alphas[alphaCounter]            
            changesMade = True
            while changesMade:
                changesMade = False
                counter = 0
                while not changesMade and counter < len(alpha)-1:
                    if alpha[counter]!=alpha[counter+1] and alpha[counter].lower() == alpha[counter+1].lower():
                        alpha = alpha.replace(alpha[counter] + alpha[counter+1], "")
                        changesMade = True
                    counter+=1
            alphas[alphaCounter] = alpha
            alphaCounter+=1
        
        lengths = []
        for alpha in alphas[:]:
            lengths.append(len(alpha))
        
        lengths.sort()        
        print("Length = " + str(lengths[0]))

Main().run()
    
