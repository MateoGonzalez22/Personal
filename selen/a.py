import time

file = open("spanish wordlist.txt")

silaba = input("Igrese silaba: ")

def array():

    wordlist = []

    for i in file:
        wordlist.append(i)

    start = time.time()

    for i in wordlist:
        if (i.find(silaba) >= 0):
            print(i)
            break

    print("Tiempo total: " + str((time.time() - start)))



def archivo():

    start = time.time()

    for i in file:
        if (i.find(silaba) >= 0):
            print(i)
            break

    print("Tiempo total: " + str((time.time() - start)))


archivo()