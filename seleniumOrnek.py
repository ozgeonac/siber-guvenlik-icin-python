from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://www.python.org")
if "Python" in driver.title:
    print("Baslikta python var")
