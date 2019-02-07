from selenium import webdriver

driver = webdriver.Chrome("C:/Users/Harish/PycharmProjects/Class_6/drivers/chromedriver.exe")
driver.get("https://www.makemytrip.com/")
driver.implicitly_wait(30)
driver.find_element_by_id("header_tab_hotels").click()
driver.find_element_by_id("header_tab_holidays").click()
driver.back()
driver.forward()
driver.quit()
