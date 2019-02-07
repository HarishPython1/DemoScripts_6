import time
from selenium import webdriver

browser = 'chrome'

if browser=='chrome':
    driver = webdriver.Chrome(executable_path="C:/Users/Harish/PycharmProjects/Class_6/drivers/chromedriver.exe")
    #driver = webdriver.Chrome()
    #driver.get("https://www.makemytrip.com/")
elif browser=='firefox':
    driver = webdriver.Firefox(executable_path="C:/Users/Harish/Documents/drivers/geckodriver.exe")
    #driver = webdriver.Firefox()
    #driver.get("https://www.makemytrip.com/")
elif browser == 'ie':
    driver = webdriver.Ie(executable_path="C:/Users/Harish/Downloads/IEDriverServer_Win32_3.14.0/IEDriverServer.exe")
    #driver = webdriver.Ie()
else :
    print("Error - Provide appropriate browser name")

driver.get("https://www.makemytrip.com/")
driver.maximize_window()
driver.find_element_by_id("header_tab_hotels").click()
time.sleep(5)
driver.quit()
