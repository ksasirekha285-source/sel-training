import time

from selenium import webdriver
opts =webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)

driver =webdriver.Chrome(opts)

driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)


# driver.find_element('xpath','//table[@name="BookTable"]//tr[2]/td[1]')
# driver.find_element('xpath','//table[@name="BookTable"]//tr[2]/td[2]')
# driver.find_element('xpath','//table[@name="BookTable"]//tr[2]/td[3]')
# driver.find_element('xpath','//table[@name="BookTable"]//tr[2]/td[4]')


for r in range(2,8):
    for c in range(1,5):
        data= driver.find_element('xpath',f'//table[@name="BookTable"]//tr[{r}]/td[{c}]')
        print(data.text, end='\t\t')
    print()

