# coding=utf-8
from selenium import webdriver
import unittest
import time

class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.youdao.com "

    def test_youdao(self):
        driver=self.driver
        driver.get(self.base_url+'/')
        driver.find_element_by_xpath("//input[@id='translateContent']").clear()
        driver.find_element_by_id("translateContent").send_keys("webdriver")
        driver.find_element_by_name("q").click()
        time.sleep(2)
        title=driver.title
        self.assertEqual(title,u'有道首页')

    def tearDown(self):
        # self.driver.quit()
         self.driver.close()
if __name__=="__main__":
    unittest.main()