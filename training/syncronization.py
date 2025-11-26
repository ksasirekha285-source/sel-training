# import time
#
# from selenium import webdriver
# opts =webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
#
# driver =webdriver.Chrome(opts)
# driver.implicitly_wait(45)
#
# driver.get(r'C:\Users\dhamo\PycharmProjects\selenium_training\files\progressbar.html')
# time.sleep(2)
#
# driver.find_element('xpath','//button[text()="Click Me"]').click()
#
# driver.find_element('xpath','//div[text()="100%"]')
# time.sleep(2)
#
# driver.find_element('xpath','//button[text()="Click Me"]').click()


import time

from selenium import webdriver
opts =webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)

driver =webdriver.Chrome(opts)
driver.implicitly_wait(45)

driver.get(r'C:\Users\dhamo\PycharmProjects\selenium_training\files\loading.html')
time.sleep(2)

driver.find_element('xpath','//input[@name="fname"]').send_keys('sasi')
time.sleep(2)
driver.find_element('xpath','//input[@name="lname"]').send_keys('rekha')


