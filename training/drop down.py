import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

opts =webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)

driver =webdriver.Chrome(opts)


driver.get('https://www.facebook.com/r.php?entry_point=login')
driver.maximize_window()
time.sleep(2)



# from selenium import webdriver
# import time
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver = webdriver.Chrome(opts)
# driver.get("file:///C:/Users/Admin/Desktop/dd.html")
# driver.maximize_window()
# time.sleep(3)
# """ # Way2: """
# from selenium.webdriver import Chrome,ChromeOptions
# opts = ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver = Chrome(opts)
# """ from selenium import webdriver #
# from selenium.webdriver.support.select import Select
# import time opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True) """
# driver = webdriver.Chrome(opts)
# driver.get("file:///C:/Users/Admin/Desktop/dd.html")
# driver.maximize_window()
# time.sleep(3)
# food_dropdown = driver.find_element("xpath","//select[@id='a1']")
# ssd = Select(food_dropdown)
# ssd.select_by_index(1)
# """ from selenium.webdriver.support.select import Select driver = webdriver.Chrome(opts) driver.get("https://www.facebook.com/r.php?entry_point=login") driver.maximize_window() time.sleep(3) day_dropdown = driver.find_element("xpath","//select[@id='day']") ssd = Select(day_dropdown)
# ssd.select_by_index(26) Oct 16, 2:31 PM
# #
# # year_dd = driver.find_element('id','//select[@id="year"]')
# # ssd=Select(year_dd)
# # ssd.select_by_visible_text("1915")