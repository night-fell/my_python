from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get("http://m.wecash.net/wep/user/login.html")

#driver.add_cookie({'name': '_ga', 'value': 'GA1.2.1048472950.1488344844'})
# driver.add_cookie({'name': '_zg', 'value': '%7B%22uuid%22%3A%20%2215980ff81684e1-04fb3cff2ab9cd-574e6e46-4a640-15980ff8169a5%22%2C%22sid%22%3A%201490876200.818%2C%22updated%22%3A%201490876345.562%2C%22info%22%3A%201490804724318%2C%22cuid%22%3A%20%22EFB1B7C904426746A10780AD02139B29%22%7D'})

driver.find_elements_by_xpath()

driver.refresh()

username = driver.find_element_by_class_name("login-input").text
print(username)

print driver.title
driver.quit()
