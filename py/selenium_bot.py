import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import threading
import signal

checkPrice_stop = False

def checkPrice(driver, price_label):
    driver.get("https://coinmarketcap.com/es/currencies/ethereum/")
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "priceValue")))
    print("encontro")
    while True:
        if checkPrice_stop:
            driver.quit()
            break
        texto = driver.find_element(By.CLASS_NAME, "priceValue").text
        price_label.configure(text=texto)
        time.sleep(1)



class bot:

    driver = None

    def run(price_label):
        
        chrome_options = Options()
        """ chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--headless") """
        bot.driver = webdriver.Chrome(executable_path="./chromedriver" ,options =chrome_options)
        driver = bot.driver
        
        
        task = threading.Thread(target=checkPrice, args=(driver, price_label))
        task.start()

        global checkPrice_stop
        




        

    def quit():
        print(bot.driver)
        bot.driver.quit()
        




