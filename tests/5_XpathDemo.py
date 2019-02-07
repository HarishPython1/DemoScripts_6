from selenium import webdriver

browser = 'chrome1'

if browser == 'chrome':driver = webdriver.Chrome(executable_path="C:/Users/Harish/PycharmProjects/Class_6/drivers/chromedriver.exe")
elif browser == 'firefox':driver = webdriver.Firefox(executable_path="C:/Users/Harish/Documents/drivers/geckodriver.exe")
elif browser == 'ie':driver = webdriver.Ie(executable_path="C:/Users/Harish/Downloads/IEDriverServer_Win32_3.14.0/IEDriverServer.exe")
else : print("Error - Provide appropriate browser name")
driver.get("https://www.makemytrip.com/")
driver.maximize_window()

#1st-Way

