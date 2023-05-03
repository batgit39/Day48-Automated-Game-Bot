# go to wikipedia and search python in searchbar
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service('/home/mitresh/Development-Selenium/chromedriver'))
driver.maximize_window()

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# articles_number = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[1]/div/div[3]/a[1]")
# print(articles_number.get_attribute('innerHTML'))
# articles_number.click()


search= driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
