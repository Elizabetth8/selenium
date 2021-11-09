# Chapter 13: Selenium
## Title 2 text
### title 3 

# Selenium WebDriver with Python

## Selenium Setup

1. Download the selenium
go to the Terminal (pycharm)
    ```python
    pip install selenium # library, code written by developers
   pip freeze # to check the selenium is in the list
    ```
2. Download Chromedriver
   - check the version of your chrome browser (if you dont have Chrome browser, download it)
   - download the ChromDriver:  [driver website](https://chromedriver.chromium.org/downloads)
   - select the right one
   - extract the downloaded folder and cope the chromdrive file
3. Save in the Python main location 
   - go to Python main folder
   - 
4. Import Selenium, run sample code
```python
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.yahoo.com/")
```

## What is HTML document?
 - Document Object Module - html document (DOM)
 - Tag: head, body, div, button, span, input (text, password, submit and etc.) 
 ```html
<head></head>
<body></body>
```
### Using Chrome developers tools options to inspect web elements:
   - Tags are purple
   - Attributes are in red
   - Values of attributes are in blue
   - Text in the elements, that are in tags, are black

### Finding the element :

```python
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.google.com/")
driver.maximize_window()
# Mostly used: (4)
driver.find_element_by_id()  # fastest way of finding element
driver.find_element_by_name()
driver.find_element_by_xpath() # technics
driver.find_element_by_css_selector() # technics

driver.find_element_by_link_text()
driver.find_element_by_class_name() # class might me dynamic
```
### Agenda for Selenium:
- Webdriver - handling the browser
- Webelement - working with element
- Framework - manage the code better
