from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

timeout = time.time() + 5
five_min = time.time() + 60*5

#setup selenium
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(''))
# add your driver path 
driver.maximize_window()

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]

def get_item_prices():
    prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
    item_prices = []
    final_dict = {}
        
    for p in prices:
        text = p.text
        if text != "":
            cost = int(text.split("-")[1].strip().replace(",", ""))
            item_prices.append(cost)
        
    for n in range(len(item_prices)):
        final_dict[item_prices[n]] = item_ids[n]
        
    return final_dict

def get_total_cookies():
    money_element = driver.find_element(By.ID,"money").text
    if "," in money_element:
        money_element = money_element.replace(",", "")
        
    return int(money_element)

def get_purchasable_items(item_prices_dict, cookie_count):
    upgradable = {}
    for cost, id in item_prices_dict.items():
        if cookie_count > cost:
            upgradable[cost] = id
        
    return upgradable

def get_to_purchase_id(purchasable_items):
    highest_price_affordable_upgrade = max(purchasable_items)
    print(highest_price_affordable_upgrade)
    return purchasable_items[highest_price_affordable_upgrade]

def main():
    cookie.click()
    global timeout
    if time.time() > timeout:
        item_prices_dict = get_item_prices()       
        cookie_count = get_total_cookies()
        purchasable_items = get_purchasable_items(item_prices_dict, cookie_count)
        to_purchase_id = get_to_purchase_id(purchasable_items)
        
        driver.find_element(By.ID, to_purchase_id).click()
        
        #Add another 5 seconds until the next check
        timeout = time.time() + 5
        
    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(cookie_per_s)

while True:
    main()
