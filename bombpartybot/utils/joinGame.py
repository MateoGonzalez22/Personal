from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def joinGame(driver):

    while(True):

        try:
            WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='seating']")))
            #WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-text='joinGame']"))).click()
            driver.find_element(By.XPATH, "//button[@data-text='joinGame']").click()

            

            break
            
        except:
            print("\nLa partida esta en curso")
            input("Presione ENTER cuando termine: ")

        
    
