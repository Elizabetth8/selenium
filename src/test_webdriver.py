import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Lets open automation demo website
driver.get("http://automationpractice.com/index.php")
driver.maximize_window()

search_box = driver.find_element(By.XPATH, "//input[@id='search_query_top']")
search_box.send_keys('dress' + Keys.ENTER)

time.sleep(5)

#result = driver.find_element(By.CSS_SELECTOR, 'span.heading-counter').text
#print('print the result of the search:', result)

print('#################### 11/07/2021 ###############')
print('############## Example for find Elements ##########')
products = driver.find_elements(By.XPATH, '//div[@id="center_column"]//a[@class="product-name"]')
product_names =[]
for product in products:
    print(product.text)
    product_names.append(product.text.strip())
print(product_names)
print('-------------completed------------')

#driver.quit()