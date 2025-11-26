# import time
# import pytest
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# @pytest.mark.parametrize("username,pwd",[('standard_user','secret_sauce'),('standard','secret'),('hiking','spki87yu')])
# def test_login(username,pwd):
#     driver.get('https://www.saucedemo.com/')
#     time.sleep(2)
#     driver.find_element('id',"user-name").send_keys(username)
#     time.sleep(2)
#     driver.find_element('id', "password").send_keys(pwd)
#     time.sleep(2)
#     driver.find_element('id', "login-button").click()
#     time.sleep(2)
#
#     if 'inventory' in driver.current_url:
#         print("successful login")
#     else:
#         print("unsuccessful login")


import time
import pyreference

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
wait_ = WebDriverWait(driver, 10)

driver.get('https://www.saucedemo.com/')
time.sleep(2)


@pyreference.mark.dependency()
def test_login():

    driver.find_element('id',"user-name").send_keys('standard_user')
    time.sleep(2)
    driver.find_element('id', "password").send_keys('secret_saucee')
    time.sleep(2)
    driver.find_element('id', "login-button").click()
    time.sleep(2)
    wait_.until(expected_conditions.visibility_of_element_located('xpath','//span[text()="Products"]'))

@pyreference.mark.dependency(depends=['test_login'])             ## dependent testcase
def test_logout():
    driver.find_element('id', 'react-burger-menu-btn').click()
    time.sleep(2)
    driver.find_element('id', 'logout_sidebar_link').click()