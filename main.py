from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("http://www.yahoo.com")
input_field = browser.locator.css_selector('input[type="text"]')
input_field.send_keys("今日のウマ娘のニュース")

# Submit the search form
input_field.send_keys(Keys.RETURN)
