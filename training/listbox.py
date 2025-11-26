import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver = webdriver.Chrome(opts)
driver.get("https://www.myntra.com/")
driver.find_element("name",'q').send_keys('iphone')
time.sleep(3)