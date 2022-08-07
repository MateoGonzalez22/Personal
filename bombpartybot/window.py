import createRoom
import joinRoom
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



#from selenOrdenado import connectToRoom.createRoom
def window():

    firefox_options = Options()

    firefox_options.add_argument("--no-sandbox")
    firefox_options.add_argument("--disable-extensions")
    firefox_options.add_argument("--disable-gpu")
    firefox_options.add_argument("--headless")
    driver = webdriver.Firefox(options = firefox_options)

    # driver = webdriver.Firefox()

    
    while(True):

        print("////////////////////////////////////////////////////\n")

        num = input("1- Crear sala\n2- Entrar a una sala\n\nIngresar: ")

        if(num == "1"):
                
            createRoom.createRoom(driver, "tute's room" , "tute's bot")
            break

        elif(num == "2"):
            
            codigo = input("\nIngrese el codigo de sala: ")

            if (len(codigo) != 4):
                print("\nEl codigo es de 4 caracteres!")
                break
            else:
                joinRoom.joinRoom(driver, "tute's bot", codigo)
                break
        
        else:

            print("\nIncorrecto!\n")







window()


