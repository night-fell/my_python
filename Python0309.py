
# -*- coding:UTF-8 -*-
"""
__author__:liqing

python网站selenium示例
脚本中有部分做了简单调试

"""
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
# Get local session of firefox
browser = webdriver.Firefox()
# Load page
browser.get("http://www.yahoo.com")
assert "Yahoo" in browser.title
# Find the query box
elem = browser.find_element_by_name("p")
elem.send_keys("seleniumhq" + Keys.RETURN)
# Let the page load, will be added to the API
time.sleep(2)
try:
    browser.find_element_by_xpath("//a[contains(@href,'http://seleniumhq.org')]")
except NoSuchElementException:
    assert '0', "can't find seleniumhq"
browser.quit()

