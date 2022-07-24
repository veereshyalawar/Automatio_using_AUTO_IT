import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class Autoit:
    def uplodfile(self):

        serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
        driver = webdriver.Chrome(service=serv_obj)
        driver.maximize_window()
        driver.get("https://smallpdf.com/pdf-converter")
        time.sleep(3)
        driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[2]/button/div/span').click()
        driver.find_element(By.XPATH,'//*[@id="__cond-31"]/div/div/div/div/div/div/form/label/div/div[2]/div/button[1]/span').click()
        release_file = (r"C:\Users\veeresh\Documents\AutoIt.exe")
        os.system(release_file)
        time.sleep(10)
        driver.close()

Auto = Autoit()
Auto.uplodfile()