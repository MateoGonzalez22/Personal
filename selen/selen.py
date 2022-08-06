from argparse import Action
from tabnanny import check
import click
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import wordFinder
from selenium.webdriver.firefox.options import Options
import repeated

firefox_options = Options()

firefox_options.add_argument("--no-sandbox")
firefox_options.add_argument("--disable-extensions")
firefox_options.add_argument("--disable-gpu")
firefox_options.add_argument("--headless")
driver = webdriver.Firefox(options=firefox_options)



def joinGame():
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-text='joinGame']"))).click()


def connectToRoom():

    if(input("Ingrese 1 para crear la sala o 2 para unirse a una sala: ") == "2"):

        #driver.get(input("Ingrese el link de la sala: "))
        driver.get("https://jklm.fun/UCHG")

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='styled nickname']")))
        nickName = driver.find_element(By.XPATH, "//input[@class='styled nickname']")
        nickName.clear()
        nickName.send_keys("tute's bot")
        driver.find_element(By.XPATH, "//button[@class='styled']").click()
        time.sleep(4)
        driver.find_element(By.XPATH, '//button[@class="toggleMute"]').click()
        driver.switch_to.frame(0)
        joinGame()
        
        checkIfStarted()
        
        time.sleep(100)



def matchStarted():

    while(True):
        print("empezo")

        #WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//input[@type="text"]')))

        WebDriverWait(driver, 120).until(EC.invisibility_of_element_located((By.XPATH, "//div[@class='seating']")))

        seating = driver.find_element(By.XPATH, "//div[@class='seating']")

        while(seating.is_displayed() == False):
            
            turn = driver.find_element(By.XPATH, '//input[@type="text"]')

            while(turn.is_displayed()):

                syllable = checkSyllable().upper()

                word = wordFinder.findWord(syllable)

                repeated.appendRepeated(word)

                turn.send_keys(word)
                turn.send_keys(Keys.ENTER)

                time.sleep(1)

            # print("Turno del rival")

            time.sleep(0.5)

        # print("termino la partida")

        joinGame()

        try:
            WebDriverWait(driver, 120).until(EC.invisibility_of_element_located((By.XPATH, "//div[@class='seating']")))

        except:
            print("La partida nunca comenzó...")
            driver.close()




def checkIfStarted():

    try:
        WebDriverWait(driver, 120).until(EC.invisibility_of_element_located((By.XPATH, "//div[@class='seating']")))
        timeToStart = True

    except:
        print("La partida nunca comenzó...")
        driver.close()

    if (timeToStart):
        matchStarted()



def checkSyllable():

    WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='syllable']")))
    syllable = driver.find_element(By.XPATH, "//div[@class='syllable']").text
    return syllable
    


connectToRoom()


time.sleep(500)


driver.close()


#https://selenium-python.readthedocs.io/waits.html#:~:text=Selenium%20Webdriver%20provides%20two%20types,trying%20to%20locate%20an%20element.