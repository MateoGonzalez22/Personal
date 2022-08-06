import repeated

def findWord(syllable):

    file = open("englishWordlist.txt", "r")
    repeatedWords = repeated.repeatedWords


    for i in file:

        if i.find(syllable) >= 0:
            
            if(i not in repeatedWords):
                return i
            else:
                continue


            


