# import time
# from reading_excel import excel_read
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# data = excel_read()
# print(data)
#
#
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//a[@class="ico-register"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//input[@id="gender-male"]').click()
# driver.find_element('xpath', '//input[@id="FirstName"]').send_keys('James')
# driver.find_element('xpath', '//input[@id="LastName"]').send_keys('Watt')
# driver.find_element('xpath', '//input[@id="Email"]').send_keys('james@gmail.com')
# driver.find_element('xpath', '//input[@id="Password"]').send_keys('james@12345')
# driver.find_element('xpath', '//input[@id="ConfirmPassword"]').send_keys('james@12345')

import time
from reading_excel import excel_read

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
# data = excel_read()
# print(data)


driver.get('https://demowebshop.tricentis.com/')
time.sleep(2)


class TestRegister:

 def test_reg(self):
    driver.find_element('xpath', '//a[@class="ico-register"]').click()
   time.sleep(2)
 def test_gender(self):
    driver.find_element('xpath', '//input[@id="gender-male"]').click()
 def test_fname(self):
    driver.find_element('xpath', '//input[@id="FirstName"]').send_keys('James')
 def test_lname(self):
    driver.find_element('xpath', '//input[@id="LastName"]').send_keys('Watt')
 def test_email(self):
    driver.find_element('xpath', '//input[@id="Email"]').send_keys('james@gmail.com')
 def test_password(self):
    driver.find_element('xpath', '//input[@id="Password"]').send_keys('james@12345')
    driver.find_element('xpath', '//input[@id="ConfirmPassword"]').send_keys('james@12345')
