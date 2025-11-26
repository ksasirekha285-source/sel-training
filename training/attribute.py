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
# beauty = driver.find_element('xpath','//a[text()="Beauty"][1]')
# print(beauty.get_attribute('href'))
# print(beauty.get_attribute('class'))
# print(beauty.get_attribute('style'))
# print(beauty.get_attribute('data-type'))
# print(beauty.text)




import time

from selenium import webdriver
opts =webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)

driver =webdriver.Chrome(opts)

driver.get("https://www.python.org/")
time.sleep(2)

all_links = driver.find_elements('tag name','a')

for link in all_links:
    print(link.get_attribute('href'))

