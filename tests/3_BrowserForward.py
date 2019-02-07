import time
from selenium import webdriver

driver = webdriver.Chrome("C:/Users/Harish/PycharmProjects/Class_6/drivers/chromedriver.exe")
driver.get("https://www.makemytrip.com/")
driver.find_element_by_id("header_tab_hotels").click()
time.sleep(5)
driver.find_element_by_id("header_tab_holidays").click()
time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)
driver.quit()
