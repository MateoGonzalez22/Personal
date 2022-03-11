import os
import time

i = 0
espacio = " "

while i < 10:
    os.system("clear")
    espacio = espacio + " a"
    print(espacio)
    time.sleep(1)
    i+=1
    if i == 5:
        for x in range(0,5):
            espacio[x] = ""
    