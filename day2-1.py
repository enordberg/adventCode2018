#filePath = "day2Puzzle1Sample.txt"
filePath = "day2Puzzle1.txt"

numberOfTwos = 0
numberOfThrees = 0
with open(filePath) as fp:  
   line = fp.readline()
   while line:
       charactersChecked = []
       hasTwo = False
       hasThree = False
       for c in line:
           if (c in charactersChecked):
               continue                
           charactersChecked.append(c)
           characterCount = line.count(c)
           if (characterCount==2):
               hasTwo = True
           if (characterCount==3):
               hasThree = True               
           if (hasTwo and hasThree):
               break
       if (hasTwo):
           numberOfTwos+=1
       if (hasThree):
           numberOfThrees+=1           
       line = fp.readline()
print("number of twos " + str(numberOfTwos))
print("number of threes " + str(numberOfThrees))
print("checksum " + str(numberOfTwos * numberOfThrees))