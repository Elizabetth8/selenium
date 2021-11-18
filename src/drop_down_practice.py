import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://automationpractice.com/index.php")
driver.maximize_window()

pickdrop = driver.find_element(By.XPATH, "//header/div[3]/div[1]/div[1]/div[6]/ul[1]/li[1]/a[1]").click()
choose = driver.find_element(By.XPATH, "//header/div[3]/div[1]/div[1]/div[6]/ul[1]/li[1]/ul[1]/li[2]/ul[1]/li[1]/a[1]").click()
