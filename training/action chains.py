import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

opts =webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)

driver =webdriver.Chrome(opts)

ac_obj=ActionChains(driver)
#
# driver.get('https://www.myntra.com/')
# time.sleep(2)

# men =driver.find_element('xpath','//a[text()="Men"][1]')
# ac_obj.move_to_element(men).perform()
# time.sleep(2)
# kids =driver.find_element('xpath','//a[text()="Kids"][1]')
# ac_obj.move_to_element(kids).perform()
# time.sleep(2)
# beauty =driver.find_element('xpath','//a[text()="Beauty"][1]')
# ac_obj.move_to_element(beauty).perform()
# time.sleep(2)

#
#
# #to scroll till the end of application
# ac_obj.send_keys(Keys.END).perform()
# time.sleep(1)
# ac_obj.send_keys(Keys.HOME).perform()
# time.sleep(1)
# ac_obj.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(2)
# ac_obj.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(2)
# ac_obj.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(2)
# ac_obj.send_keys(Keys.PAGE_UP).perform()
# time.sleep(2)
# ac_obj.send_keys(Keys.PAGE_UP).perform()
# time.sleep(2)
# ac_obj.send_keys(Keys.PAGE_UP).perform()
# time.sleep(2)

driver.get('https:https://testautomationpractice.blogspot.com/')
time.sleep(2)

ele=driver.find_element('xpath','')
ac_obj.scroll_to_element(ele).perform()
time.sleep(2)

draggable_ele =driver.find_element('xpath','')
droppable_ele=driver.find_element('xpath','')