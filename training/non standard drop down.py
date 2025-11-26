# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option('detach',True)
#
# driver=webdriver.Chrome(opts)
# driver.implicitly_wait(30)
#
# driver.get("https://www.ksrtc.in/")
# time.sleep(2)
#
# driver.find_element('xpath',)
##############################################################################


# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option('detach',True)
#
#
# driver = webdriver.Chrome(opts)
# driver.get("https://www.amazon.in/")
# time.sleep(3)
# driver.refresh()
# time.sleep(3)
# driver.find_element("id","twotabsearchtextbox").send_keys("shoes")
# time.sleep(3)
# data = driver.find_elements("xpath","//div[@class='s-suggestion s-suggestion-ellipsis-direction']")

##################################################################################################################


import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver = webdriver.Chrome(opts)
driver.get("https://www.flipkart.com/")
driver.find_element("name",'q').send_keys('iphone')
time.sleep(3)

data=driver.find_elements('xpath','//div[@class="YGcVZO _2VHNef"]')
time.sleep(3)
option= input("enter your option :").lower()
time.sleep(3)
for i in data:
     if option in i.text:
        i.click()
        break
time.sleep(3)
