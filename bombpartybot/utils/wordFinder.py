import utils.usedWords as usedWords

def findWord(syllable):

    file = open("utils/wordLists/english.txt")

    for i in file:

        if i.find(syllable) >= 0:
            
            if(i not in usedWords.usedWordsArray):
                return i
            else:
                continue
    