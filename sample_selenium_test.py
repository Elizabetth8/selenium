from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.google.com/")
driver.maximize_window()
#search_box = driver.find_element_by_name('q')
# - search for selenium
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('selenium') # entering the text in the input (text) form (search box)
search_box.send_keys(Keys.ENTER)

# - capture the result text

result_msg = driver.find_element(By.ID, 'result-stats').text
print('I got the result here: \n\t', result_msg)

# -Close the browser
driver.close()


