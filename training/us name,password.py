import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


opts =webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)

driver =webdriver.Chrome(opts)
driver.implicitly_wait(45)

wait_obj=WebDriverWait(driver,20)

driver.get('https://www.saucedemo.com/')
time.sleep(2)

driver.find_element('id','user-name').send_keys('standard_user')
time.sleep(2)
driver.find_element('id','password').send_keys('secret_sauce')
time.sleep(2)
driver.find_element('id','login-button').click()
time.sleep(2)



try:
    wait_obj.until(expected_conditions.visibility_of_element_located(('xpath','//span[text()="Products"]')))
    print("succesfull login")
# error_msg=driver.find_element('xpath','//h3[@data-test="error"]')
# time.sleep(2)

except:
    print("unsuccesfull login")