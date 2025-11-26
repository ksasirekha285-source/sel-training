'''
css selector    :   To locate the web-elements using any attribute
                    SYNTAX  :   tagname[attr_name="attr_value"]


'''
import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://www.saucedemo.com/')
time.sleep(2)

driver.find_element('css selector', 'input[placeholder="Username"]').send_keys('standard_user')
time.sleep(1)
driver.find_element('css selector', 'input[type="password"]').send_keys('secret_sauce')
time.sleep(1)
driver.find_element('css selector', 'input[type="submit"]').click()




