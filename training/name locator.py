# import time
#
# from selenium import webdriver
# opts =webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
#
# driver =webdriver.Chrome(opts)
#
# driver.get("https://demowebshop.tricentis.com/")
# time.sleep(2)
#
# driver.find_element('class name','ico-register').click()
# time.sleep(2)
# driver.find_element('class name','ico-login').click()
# time.sleep(2)
# driver.find_element('class name','ico-cart').click()
# time.sleep(2)


import time

from selenium import webdriver
opts =webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)

driver =webdriver.Chrome(opts)

driver.get(r"C:\Users\dhamo\PycharmProjects\selenium_training\files\css_selector.html")
time.sleep(2)

driver.find_element('tag name','input').send_keys('sasirekha')
time.sleep(2)
driver.find_element('tag name','input').send_keys('asdfghj')
time.sleep(2)
