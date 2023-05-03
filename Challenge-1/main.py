# go to python.org and print data about events
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service('/home/mitresh/Development-Selenium/chromedriver')
driver = webdriver.Chrome(service=s)

driver.get("https://www.python.org/")

menu = driver.find_element(By.XPATH, "/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul")

time_elements = menu.find_elements(By.TAG_NAME, "time")
time = [] 
for t in time_elements:
    year = t.find_element(By.CLASS_NAME, "say-no-more")
    time.append(year.get_attribute('innerHTML') + t.text)

names = menu.find_elements(By.TAG_NAME, "a")
name = []
for n in names:
    name.append(n.get_attribute('innerHTML'))

events = {}
for x in range(len(time)):
    events[x] = {
            "time": time[x],
            "name": name[x]
            }

print(events)

driver.quit()
