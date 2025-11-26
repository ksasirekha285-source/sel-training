# import time
#
# from selenium import webdriver
# opts =webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
#
# driver =webdriver.Chrome(opts)
#
# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(2)
#
# driver.find_element('xpath','//button[@id="alertBtn"]').click()
# alert_obj = driver.switch_to.alert
#
# alert_obj.accept()
# time.sleep(2)
##################################
# import time
#
# from selenium import webdriver
# opts =webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
#
# driver =webdriver.Chrome(opts)
#
# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(2)
#
# driver.find_element('xpath','//button[@id="confirmBtn"]').click()
# alert_obj = driver.switch_to.alert
# time.sleep(2)
# alert_obj.accept()
# time.sleep(2)
#
# driver.find_element('xpath','//button[@id="confirmBtn"]').click()
# time.sleep(2)
#
# alert_obj.dismiss()
###########################################

# import time
#
# from selenium import webdriver
# opts =webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
#
# driver =webdriver.Chrome(opts)
#
# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(2)
#
# driver.find_element('xpath','//button[@id="promptBtn"]').click()
# alert_obj = driver.switch_to.alert
# time.sleep(2)
#
# alert_obj.send_keys("sasi rekha")
#
# alert_obj.accept()
# time.sleep(2)

# #######################################################
# import time
#
# from selenium import webdriver
# opts =webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
#
# driver =webdriver.Chrome(opts)
#
# driver.get("https://the-internet.herokuapp.com/basic_auth")
# time.sleep(2)
#
# driver.find_element('xpath','//button[@id="promptBtn"]').click()
# alert_obj = driver.switch_to.alert
# time.sleep(2)
#
# alert_obj.send_keys("sasi rekha")
#
# alert_obj.accept()
# time.sleep(2)

# import time
#
# from selenium import webdriver
# opts =webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
#
# driver =webdriver.Chrome(opts)
#
# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(2)
#
# file1=r'C:\Users\dhamo\PycharmProjects\selenium_training\files\css_selector.html'
# file2=r'C:\Users\dhamo\PycharmProjects\selenium_training\files\css_selector_dup.html'
#
# driver.find_element('xpath','//input[@id="singleFileInput"]').send_keys(file1)

#
# import time
#
# from selenium import webdriver
# opts =webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
#
# driver =webdriver.Chrome(opts)
#
# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(2)
#
# file1=r'C:\Users\dhamo\PycharmProjects\selenium_training\files\css_selector.html'
# file2=r'C:\Users\dhamo\PycharmProjects\selenium_training\files\css_selector_dup.html'
#
# driver.find_element('xpath','//input[@id="multipleFilesInput"]').send_keys(f'{file1}\n{file2}')


#
# import time
#
# from selenium import webdriver
# opts =webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# opts.add_argument("--disable-notifications")
# driver =webdriver.Chrome(opts)
#
# driver.get("https://www.irctc.co.in/nget/train-search")
# time.sleep(2)



import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


opts =webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)

driver =webdriver.Chrome(opts)
# driver.implicitly_wait(45)

wait_obj=WebDriverWait(driver,20)

driver.get(r'C:\Users\dhamo\PycharmProjects\selenium_training\files\loading.html')

wait_obj.until(expected_conditions.visibility_of_element_located(('xpath','//div[contains(text(),"FirstName")]')))

driver.find_element('xpath', '//input[@name="fname"]').send_keys('Jaya')
time.sleep(1)
driver.find_element('xpath', '//input[@name="lname"]').send_keys('shree')