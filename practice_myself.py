import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.google.com/')
driver.maximize_window()
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('bmw i8' + Keys.ENTER)
image_tab = driver.find_element(By.XPATH, "//body/div[@id='main']/div[@id='cnt']/div[@id='top_nav']/div[@id='hdtb']/div[@id='pTwnEc']/div[@id='hdtb-msb']/div[1]/div[1]/div[2]/a[1]")
image_tab.click()
open_image = driver.find_element(By.XPATH, "//body/div[2]/c-wiz[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/div[1]/div[1]/div[11]/a[1]/div[1]/img[1]")
open_image.click()
visit_website = driver.find_element(By.XPATH, "//body/div[2]/c-wiz[1]/div[3]/div[2]/div[3]/div[1]/div[1]/div[3]/div[2]/c-wiz[1]/div[1]/div[1]/div[3]/div[1]/a[2]/div[1]/span[1]")
visit_website.click()


time.sleep(5)
driver.quit()