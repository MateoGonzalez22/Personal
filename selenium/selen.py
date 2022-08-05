from argparse import Action
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

driver.get("https://jklm.fun/")



privateRoomButton = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//label[2]"))).click()
playButton = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[1]/div[5]/div[2]/div[1]/div[1]/form[1]/div[2]/button[1]"))).click()

# elem = driver.find_element(By.XPATH, "//div[2]/div[3]/form[1]/div[2]/input[1]")
# elem.send_keys("tute")

# enterNickname = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[2]/div[3]/form[1]/div[2]/input[1]"))).click()
enterNickname = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[2]/div[3]/form[1]/div[2]/input[1]"))).send_keys(Keys.ENTER ,"TUTE")

letras = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[2]/div[4]/div[1]/iframe[1]/html[1]/body[1]/div[2]/div[2]/div[2]/div[2]/div[1]" ))).getText()
print(letras)

# element = driver.find_element(By.XPATH, "//form[1]/div[1]/div[2]")
# element.click()


time.sleep(10)


driver.close()


#https://selenium-python.readthedocs.io/waits.html#:~:text=Selenium%20Webdriver%20provides%20two%20types,trying%20to%20locate%20an%20element.