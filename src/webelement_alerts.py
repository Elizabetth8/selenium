import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# VARIABLES
'''
Webelement class: handling js alerts, ok, cancel, entering text.
switch_to.Alert practice here:
http://courses.letskodeit.com/practice
'''
name_input_xpath = "//input[@name='enter-name']"
HOST = "http://courses.letskodeit.com/practice"
filepath = '../screenshots/'
name = "John Snow"

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.maximize_window()

# printing name
print("opening the page......")
driver.get(HOST)

print("testing the alert button......")


def test_alert_single_button():
    name_input = driver.find_element(By.XPATH, name_input_xpath)
    name_input.send_keys(name)
    # click on alert
    driver.find_element(By.ID, "alertbtn").click()
    # switch to alert
    alert = driver.switch_to.alert
    # get the text
    print("Alert text", alert.text)
    alert.accept()
    print("####### Accepted ######")


def test_alert2_multi_button():
    # enter name
    name_input = driver.find_element(By.XPATH, name_input_xpath)
    name_input.send_keys(name)
    # click on confirm
    driver.find_element(By.ID, "confirmbtn").click()
    # switch to alert
    alert2 = driver.switch_to.alert
    # get the text
    print("Alert text", alert2.text)
    # click cancel
    alert2.dismiss()
    print(" ####### canceled the alert #########")
