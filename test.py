from tkinter import *

def translateFunction(inputString):
    personalDict = readFileForPersonalDict()
    youDict = readFileForYouDict()
    maleSingularDict = readFileForMasculineSingularDict()
    malePluralDict = readFileForMasculinePluralDict()
    femaleSingularDict = readFileForFemaleSingularDict()
    femalePluralDict = readFileForFemalePluralDict()
    verbDict = readFileForVerbsDict()
    contractionDict = readFileForContractionsDict()
    adjectivesMaleSingularDict = readFileForAdjectivesMaleSingularDict()
    adjectivesMalePluralDict = readFileForAdjectivesMalePluralDict()
    adjectivesFemaleSingularDict = readFileForAdjectivesFemaleSingularDict()
    adjectivesFemalePluralDict = readFileForAdjectivesFemalePluralDict()
    print(adjectivesMaleSingularDict)
    print(adjectivesMalePluralDict)
    stringWords = inputString.split()
    fixedStringWords = expandContractions(stringWords, contractionDict)
    translation = fixFormTranslation(fixedStringWords, verbDict, maleSingularDict, malePluralDict, personalDict, youDict, femaleSingularDict, femalePluralDict, adjectivesMaleSingularDict, adjectivesMalePluralDict, adjectivesFemaleSingularDict, adjectivesFemalePluralDict)
    return translation
    


def expandContractions(stringWords, contractionDictionary):
    fixedStringWords = []
    for i in range(0,len(stringWords)):
        if stringWords[i] in contractionDictionary:
            x = contractionDictionary[stringWords[i]].split()
            for ind in range(0,len(x)):
                fixedStringWords.append(x[ind])
        else:
            fixedStringWords.append(stringWords[i])
    return fixedStringWords

            
def fixFormTranslation(fixedStringWords, verbDict, maleSingularDict, malePluralDict, personalDict, youDict, femaleSingularDict, femalePluralDict, adjectivesMaleSingularDict, adjectivesMalePluralDict, adjectivesFemaleSingularDict, adjectivesFemalePluralDict):
    translation = ""
    flagMaleSingular = False
    flagFemaleSingular = False
    flagMalePlural = False
    flagFemalePlural = False
    i = 0
    while i < len(fixedStringWords):
        
        if fixedStringWords[i] in verbDict:
            translation += verbDict[fixedStringWords[i]] + " "
            i += 1
            
        elif fixedStringWords[i] in maleSingularDict:
            flagMaleSingular = True
            flagFemaleSingular = False
            flagMalePlural = False
            flagFemalePlural = False
            if(i==0):
                translation += maleSingularDict[fixedStringWords[i]].capitalize() + " "
                i += 1
            else:
                translation += maleSingularDict[fixedStringWords[i]] + " "
                i += 1
                
        elif fixedStringWords[i] in malePluralDict:
            flagMaleSingular = False
            flagFemaleSingular = False
            flagMalePlural = True
            flagFemalePlural = False
            if(i==0):
                translation += malePluralDict[fixedStringWords[i]].capitalize() + " "
                i += 1
            else:
                translation += malePluralDict[fixedStringWords[i]] + " "
                i += 1

        elif fixedStringWords[i] in femaleSingularDict:
            flagMaleSingular = False
            flagFemaleSingular = True
            flagMalePlural = False
            flagFemalePlural = False
            if(i==0):
                translation += femaleSingularDict[fixedStringWords[i]].capitalize() + " "
                i += 1
            else:
                translation += femaleSingularDict[fixedStringWords[i]] + " "
                i += 1

        elif fixedStringWords[i] in femalePluralDict:
            flagMaleSingular = False
            flagFemaleSingular = False
            flagMalePlural = False
            flagFemalePlural = True
            if(i==0):
                translation += femalePluralDict[fixedStringWords[i]].capitalize() + " "
                i += 1
            else:
                translation += femalePluralDict[fixedStringWords[i]] + " "
                i += 1

        elif fixedStringWords[i] in personalDict:
            flagMaleSingular = True
            flagFemaleSingular = False
            flagMalePlural = False
            flagFemalePlural = False
            if(i==0):
                translation += personalDict[fixedStringWords[i]].capitalize() + " "
                i += 1
            else:
                translation += personalDict[fixedStringWords[i]] + " "
                i += 1

        elif fixedStringWords[i] in youDict:
            flagMaleSingular = True
            flagFemaleSingular = False
            flagMalePlural = False
            flagFemalePlural = False
            if(i==0):
                translation += youDict[fixedStringWords[i]].capitalize() + " "
                i += 1
            else:
                translation += youDict[fixedStringWords[i]] + " "
                i += 1

        elif fixedStringWords[i] == "the":
            if fixedStringWords[i+1] in maleSingularDict:
                flagMaleSingular = True
                flagFemaleSingular = False
                flagMalePlural = False
                flagFemalePlural = False
                if(i==0):
                    translation += maleSingularDict[fixedStringWords[i+1]].capitalize() + "ul "
                    i += 2
                else:
                    translation += maleSingularDict[fixedStringWords[i+1]] + "ul "
                    i += 2

            if fixedStringWords[i+1] in femaleSingularDict:
                
                flagMaleSingular = False
                flagFemaleSingular = True
                flagMalePlural = False
                flagFemalePlural = False
                if(i==0):
                    translation += femaleSingularDict[fixedStringWords[i+1]][:-1].capitalize() + "a "
                    i += 2
                else:
                    translation += femaleSingularDict[fixedStringWords[i+1]][:-1] + "a "
                    i += 2

            if fixedStringWords[i+1] in malePluralDict:
                flagMaleSingular = False
                flagFemaleSingular = False
                flagMalePlural = True
                flagFemalePlural = False
                if(i==0):
                    translation += malePluralDict[fixedStringWords[i+1]].capitalize() + "i "
                    i += 2
                else:
                    translation += malePluralDict[fixedStringWords[i+1]] + "i "
                    i += 2

            if fixedStringWords[i+1] in femalePluralDict:
                flagMaleSingular = False
                flagFemaleSingular = False
                flagMalePlural = False
                flagFemalePlural = True
                if(i==0):
                    translation += femalePluralDict[fixedStringWords[i+1]].capitalize() + "le "
                    i += 2
                else:
                    translation += femalePluralDict[fixedStringWords[i+1]][:-1] + "le "
                    i += 2

        elif (fixedStringWords[i] in adjectivesMaleSingularDict and flagMaleSingular):
            if(i==0):
                translation += adjectivesMaleSingularDict[fixedStringWords[i]].capitalize() + " "
                i += 1
            else:
                translation += adjectivesMaleSingularDict[fixedStringWords[i]] + " "
                i += 1

        elif fixedStringWords[i] in adjectivesMalePluralDict and flagMalePlural:
            if(i==0):
                translation += adjectivesMalePluralDict[fixedStringWords[i]].capitalize() + " "
                i += 1
            else:
                translation += adjectivesMalePluralDict[fixedStringWords[i]] + " "
                i += 1

        elif fixedStringWords[i] in adjectivesFemaleSingularDict and flagFemaleSingular:
            print(adjectivesFemaleSingularDict)
            if(i==0):
                translation += adjectivesFemaleSingularDict[fixedStringWords[i]].capitalize() + " "
                i += 1
            else:
                translation += adjectivesFemaleSingularDict[fixedStringWords[i]] + " "
                i += 1

        elif fixedStringWords[i] in adjectivesFemalePluralDict and flagFemalePlural:
            if(i==0):
                translation += adjectivesFemalePluralDict[fixedStringWords[i]].capitalize() + " "
                i += 1
            else:
                translation += adjectivesFemalePluralDict[fixedStringWords[i]] + " "
                i += 1
                    
        else:
            translation += "\"" +fixedStringWords[i] + "\" "
            i += 1
            
    return translation


def readFileForPersonalDict():
    s = open('dictionary.txt', 'r')
    line1 = s.readline()
    x = eval(line1)
    return x

def readFileForYouDict():
    s = open('dictionary.txt', 'r')
    line1 = s.readline()
    line2 = s.readline()
    x = eval(line2)
    return x

def readFileForVerbsDict():
    s = open('dictionary.txt', 'r')
    line1 = s.readline()
    line2 = s.readline()
    line3 = s.readline()
    x = eval(line3)
    return x

def readFileForMasculineSingularDict():
    s = open('dictionary.txt', 'r')
    line1 = s.readline()
    line2 = s.readline()
    line3 = s.readline()
    line4 = s.readline()
    x = eval(line4)
    return x

def readFileForFemaleSingularDict():
    s = open('dictionary.txt', 'r')
    line1 = s.readline()
    line2 = s.readline()
    line3 = s.readline()
    line4 = s.readline()
    line5 = s.readline()
    x = eval(line5)
    return x

def readFileForMasculinePluralDict():
    s = open('dictionary.txt', 'r')
    line1 = s.readline()
    line2 = s.readline()
    line3 = s.readline()
    line4 = s.readline()
    line5 = s.readline()
    line6 = s.readline()
    x = eval(line6)
    return x

def readFileForFemalePluralDict():
    s = open('dictionary.txt', 'r')
    line1 = s.readline()
    line2 = s.readline()
    line3 = s.readline()
    line4 = s.readline()
    line5 = s.readline()
    line6 = s.readline()
    line7 = s.readline()
    x = eval(line7)
    return x

def readFileForContractionsDict():
    s = open('dictionary.txt', 'r')
    line1 = s.readline()
    line2 = s.readline()
    line3 = s.readline()
    line4 = s.readline()
    line5 = s.readline()
    line6 = s.readline()
    line7 = s.readline()
    line8 = s.readline()
    x = eval(line8)
    return x

def readFileForAdjectivesMaleSingularDict():
    s = open('dictionary.txt', 'r')
    line1 = s.readline()
    line2 = s.readline()
    line3 = s.readline()
    line4 = s.readline()
    line5 = s.readline()
    line6 = s.readline()
    line7 = s.readline()
    line8 = s.readline()
    line9 = s.readline()
    x = eval(line9)
    return x

def readFileForAdjectivesFemaleSingularDict():
    s = open('dictionary.txt', 'r')
    line1 = s.readline()
    line2 = s.readline()
    line3 = s.readline()
    line4 = s.readline()
    line5 = s.readline()
    line6 = s.readline()
    line7 = s.readline()
    line8 = s.readline()
    line9 = s.readline()
    line10 = s.readline()
    x = eval(line10)
    return x

def readFileForAdjectivesMalePluralDict():
    s = open('dictionary.txt', 'r')
    line1 = s.readline()
    line2 = s.readline()
    line3 = s.readline()
    line4 = s.readline()
    line5 = s.readline()
    line6 = s.readline()
    line7 = s.readline()
    line8 = s.readline()
    line9 = s.readline()
    line10 = s.readline()
    line11 = s.readline()
    x = eval(line11)
    return x

def readFileForAdjectivesFemalePluralDict():
    s = open('dictionary.txt', 'r')
    line1 = s.readline()
    line2 = s.readline()
    line3 = s.readline()
    line4 = s.readline()
    line5 = s.readline()
    line6 = s.readline()
    line7 = s.readline()
    line8 = s.readline()
    line9 = s.readline()
    line10 = s.readline()
    line11 = s.readline()
    line12 = s.readline()
    x = eval(line12)
    return x

root = Tk()

label_1 = Label(root, text="Enter text to be translated:")
entry_TextToTranslate = Entry(root, width = 100)
text = Text(root, height = 1, width = 100)


def getEntryTextToTranslate():
    return entry_TextToTranslate.get()

def callBack():
    x = getEntryTextToTranslate()
    translation = translateFunction(x)
    text.delete(1.0, END)
    text.insert(END, translation)
    
button_Translate = Button(root, text="Translate", command=callBack)


label_1.grid(row=0,column=0)
entry_TextToTranslate.grid(row=0,column=1)
button_Translate.grid(row=0,column=2)
text.grid(row=1, column = 1)

root.mainloop()

print(translateFunction(input("Enter text to translate:")))

