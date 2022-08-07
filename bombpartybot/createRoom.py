from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import joinRoom

def createRoom(driver, roomName, botName):

    driver.get("https://jklm.fun/")

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//label[@for="gameRadio-bombparty"]'))).click()
    driver.find_element(By.XPATH, '//span[@data-text="roomPrivacy.private"]').click()
    nickname = driver.find_element(By.XPATH, '//input[@class="roomName styled"]')
    nickname.clear()
    nickname.send_keys(roomName)
    driver.find_element(By.XPATH, '//button[@data-text="play"]').click()

    joinRoom.joinRoom(driver, botName, None)


    time.sleep(10)
    driver.close()






