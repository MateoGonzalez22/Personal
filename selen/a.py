array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

import os

file = open("spanish wordlist.txt")

letra = "z"

spanish = open("spanishWordlist/" + letra + ".txt", "a")


for x in file:
    
    if (letra == x[0]):

        spanish.write(x)


