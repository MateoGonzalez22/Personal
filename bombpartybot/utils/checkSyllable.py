from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def checkSyllable(driver):

    WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='syllable']")))
    syllable = driver.find_element(By.XPATH, "//div[@class='syllable']").text
    return syllable