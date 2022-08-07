from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import utils.joinGame as utils

import bot

def joinRoom(driver, botName, codigo):
    
    if (codigo != None):

        driver.get("https://jklm.fun/" + codigo)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='styled nickname']")))
    nickName = driver.find_element(By.XPATH, "//input[@class='styled nickname']")
    nickName.clear()
    nickName.send_keys(botName)
    driver.find_element(By.XPATH, "//button[@class='styled']").click()
    time.sleep(4)
    driver.find_element(By.XPATH, '//button[@class="toggleMute"]').click()
    driver.switch_to.frame(0)

    if(codigo == None):
        print("Codigo de la sala: " + driver.current_url)
    
    utils.joinGame(driver)

    bot.bot(driver)

