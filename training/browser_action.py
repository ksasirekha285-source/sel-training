import time
start_time=time.time()
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)

driver=webdriver.Chrome(opts)

#launch the application
driver.get('https://www.myntra.com/?src=bc')
time.sleep(2)
#
# ##to maximize the window
driver.maximize_window()
time.sleep(2)
#
# ##to minimize the window
#
# driver.minimize_window()
# time.sleep(2)
#
# #to go back
# driver.back()
# time.sleep(2)
#
#to go forward
driver.forward()
time.sleep(2)
#
#to refresh
driver.refresh()
time.sleep(2)
#
# print(driver.current_url)  ##gives the url of the paage
# print(driver.title)        ##it will give the title of the page
# print(driver.name)         ##it gives the names of the browser
#
end_time=time.time()
print('total time =',end_time-start_time)


##take the screen short of the application

##driver.save_screenshot('myntra_screenshot.png')

driver.save_screenshot(r'C:\Users\dhamo\PycharmProjects\selenium_training\screen s\mynthra_ss.png')