# '''
# attribute name and value ://tag name[@att_name='attr_value']
#
# '''
# #
# # import time
# #
# # from selenium import webdriver
# # opts =webdriver.ChromeOptions()
# # opts.add_experimental_option("detach",True)
# #
# # driver =webdriver.Chrome(opts)
# #
# # driver.get("https://demowebshop.tricentis.com/")
# # time.sleep(2)
# # driver.find_element('xpath','//a[@class="ico-register"]').click()
# # driver.find_element('xpath','//input[@class="text-box single-line"]').send_keys('hari')
# # driver.find_element('xpath','//input[@data-val-required="Last name is required."]').send_keys('k')
# # driver.find_element('xpath','//input[@class="text-box single-line"]').send_keys('hari@123@gmail.com')
# # driver.find_element('xpath','//input[@class="text-box single-line password"]').send_keys('123456')
# # driver.find_element('xpath','//input[@class="text-box single-line password"]').send_keys('123456')
#
#
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
# driver.find_element('xpath','//input[@class="form-control"]').send_keys('madan')
#
# driver.find_element('xpath','//input[@placeholder="Enter EMail"]').send_keys('hari@123@gmail.com')
# driver.find_element('xpath','//input[@id="phone"]').send_keys('1236547896')
# driver.find_element('xpath','//input[@id="male"]').click()
# driver.find_element('xpath','//input[@value="friday"]').click()
#
# #
# import time
#
# from selenium import webdriver
# opts =webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
#
# driver =webdriver.Chrome(opts)
#
# driver.get("https://www.myntra.com/")
# time.sleep(2)
#
# driver.find_element('xpath','(//a[@data-type="navElements"])[1]').click()
# driver.find_element('xpath','(//a[@data-type="navElements"])[2]').click()
# driver.find_element('xpath','(//a[@data-type="navElements"])[3]').click()
# driver.find_element('xpath','(//a[@data-type="navElements"])[4]').click()
# driver.find_element('xpath','(//a[@data-type="navElements"])[5]').click()
# driver.find_element('xpath','(//a[@data-type="navElements"])[6]').click()

# import time
#
# from selenium import webdriver
# opts =webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
#
# driver =webdriver.Chrome(opts)
#
# driver.get("https://www.facebook.com/r.php?entry_point=login")
# time.sleep(2)
#
# driver.find_element('xpath','(//input[@data-type="text"])[1]').send_keys('sasi')
# driver.find_element('xpath','(//input[@data-type="text"])[2]').send_keys('dhamu')
# driver.find_element('xpath','(//input[@data-type="text"])[5]').send_keys('1256897542')


import time

from selenium import webdriver
opts =webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)

driver =webdriver.Chrome(opts)

driver.get("https://www.flipkart.com/")
time.sleep(2)

driver.find_element('xpath','//span[text()="Electronics"]').click()
driver.find_element('xpath','//span[text()="Become a Seller"]').click()
driver.find_element('xpath','//button[text()="Start Selling"]').click()