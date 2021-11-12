import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

filepath = '/screenshots/'

driver = webdriver.Chrome()
driver.get("http://automationpractice.com/index.php")
driver.maximize_window()
search_box = driver.find_element(By.XPATH, "//input[@id='search_query_top']")
search_box.send_keys('dress' + Keys.ENTER)

# Following WebDriver property/attributes or methods:
# current URL, current window handle, name, title, window-handle,
# back(), forward(), refresh(), switch_to.window(window_name)

url = driver.current_url
print('Current url:', url)
win_name = driver.current_window_handle
browser_name = driver.name
page_title = driver.title
handles = driver.window_handles

print(win_name)
print(browser_name)
print(page_title)
print(handles)
driver.save_screenshot(filepath + 'screenshot1.png')

print("########### webdriver methods #############")
# back(), forward(), refresh(), switch_to.window(window_name)
driver.back()
time.sleep(5)
print("current url:", driver.current_url)
driver.forward()
time.sleep(5)
print("current url:", driver.current_url)
time.sleep(5)
driver.refresh()

print('########## switch_to.window(window_name) ##########')
products = driver.find_elements(By.XPATH, '//div[@id="center_column"]//a[@class="product-name"]')
products[0].click()
time.sleep(2)
fb_button_xpath = '//button[@class="btn btn-default btn-facebook"]'
driver.find_element(By.XPATH, fb_button_xpath).click()
win_name = driver.window_handles
print(win_name)
print(driver.title)
time.sleep(2)
driver.switch_to.window(win_name[-1])
driver.save_screenshot(filepath + 'screenshot2.png')
driver.find_element(By.ID, 'email').send_keys("myemail@gmail.com")
driver.find_element(By.NAME, 'pass').send_keys("#YouknowNothingJohnSnow")
time.sleep(3)
driver.save_screenshot(filepath + 'screenshot3.png')
driver.close()
driver.quit()


