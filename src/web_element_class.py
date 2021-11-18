import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# VARIABLES
filepath = '../screenshots/'

driver = webdriver.Chrome()
driver.get("http://automationpractice.com/index.php")
driver.maximize_window()


def test_go_to_authentication_button():
    # click on sign in
    driver.find_element(By.XPATH, "//a[contains(text(),'Sign in')]").click()
    driver.save_screenshot(filepath + "screenshot1.png")
    time.sleep(3)


def test_create_account_button(email):
    """
    Creating account with email and static data for the sign up.
    This step is dependent on this function.
    email with @ symbol and dot to be included
    """
    # Variable:
    password = "YouKnowNothingJohnSnowIsThePassword"
    cust_fname = "Jacob"
    cust_lname = "Malkovich"
    state = "New Jersey"

    # Enter an email address to create an account mycool@email.com
    driver.find_element(By.XPATH, "//input[@id='email_create']").send_keys(email)
    # Click on create account
    driver.find_element(By.ID, "SubmitCreate").click()
    time.sleep(2)
    # radio button :click on Mrs
    mr_gender = driver.find_element(By.ID, "id_gender1")
    mr_gender.click()

    # Enter First Name
    cfirst_name = driver.find_element(By.XPATH, "//input[@id='customer_firstname']")
    cfirst_name.send_keys(cust_fname)

    # Enter Last Name
    clast_name = driver.find_element(By.XPATH, "//input[@id='customer_lastname']")
    clast_name.send_keys(cust_lname)
    time.sleep(2)
    driver.save_screenshot(filepath + "screenshot2.png")

    # Enter your password
    driver.find_element(By.ID, "passwd").send_keys(password)

    # Check sign up for our newsletter
    nl_checkbox = driver.find_element(By.ID, "newsletter")
    nl_checkbox.click()
    time.sleep(2)
    driver.save_screenshot(filepath + "screenshot3.png")

    # Verify email, get text, make sure it is what we entered
    # Verify Mr is selected
    mrs_gender = driver.find_element(By.ID, "uniform-id_gender2")
    print("Is gender type MR selected?", mr_gender.is_selected())
    print("Is gender type MRS selected?", mrs_gender.is_selected())

    # verify sign up is checked
    print("Is newsletter checkbox selected?", nl_checkbox.is_selected())

    # verify one of the error messages when required field is not entered
    address_message_xpath = "//input[@id='address1']/../span"
    address_message_element = driver.find_element(By.XPATH, address_message_xpath)
    address_message = ''
    if address_message_element.is_displayed():
        address_message = driver.find_element(By.XPATH, address_message_xpath).text
    else:
        print("Address message is not displayed")
    print("Address message displayed:", address_message)
    driver.save_screenshot(filepath + "screenshot4.png")

    # Drop down Select State
    state_dropdown = Select(driver.find_element(By.ID, "id_state"))
    state_dropdown.select_by_value("2")
    time.sleep(2)
    print("Current selection:", state_dropdown.all_selected_options[0].text)
    state_dropdown.select_by_visible_text('California')
    time.sleep(2)
    state_dropdown.select_by_index("2")


# Click on Register

# Agenda for next class
# Selenium 2 more classes:
# handling drop down list: select class (Interview mostly asked)
# handling js Alert, ok, cancel, entering text, switch_to.Alert
# explicit way: WebDriverWait class, expected_conditions class (Interview mostly asked)
# mouse movements: hover over on the elements, drag and drop: ActionChain Class

# Framework 2 classes: Pytest (unit testing), Page object modeling
