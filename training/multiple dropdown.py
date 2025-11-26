import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select


opts =webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)

driver =webdriver.Chrome(opts)

driver.get('https://www.facebook.com/r.php?entry_point=login')
time.sleep(2)
month= driver.find_element("id","month")
dd = Select(month)
data=dd.options
l=[]
for i in data:
    if i.text[0] in'aeiouAEIOU':
        l.append(i.text)
print(l)
driver.close()

