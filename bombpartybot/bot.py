from tabnanny import check
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import utils.checkSyllable as checkSyllable
import utils.wordFinder as wordFinder
import utils.usedWords as usedWords
import utils.joinGame as join

def bot(driver):

    while(True):

        try:
            WebDriverWait(driver, 60).until(EC.invisibility_of_element_located((By.XPATH, "//div[@class='seating']")))

        except:
            print("La partida tardo mas de 1 minuto en arrancar")
            driver.close()

        
        

        seating = driver.find_element(By.XPATH, "//div[@class='seating']")

        while(seating.is_displayed() == False):

            inputWord = driver.find_element(By.XPATH, '//input[@type="text"]')

            while(inputWord.is_displayed()):

                # Mi turno

                word = wordFinder.findWord(checkSyllable.checkSyllable(driver).upper())

                usedWords.appendWord(word)
                
                inputWord.send_keys(word)
                inputWord.send_keys(Keys.ENTER)

                time.sleep(1)

            # Termino mi turno

            time.sleep(0.5)
    
        # Termino la partida
        

        join.joinGame(driver)
