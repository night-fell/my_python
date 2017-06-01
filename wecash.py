# -*- coding:UTF-8 -*-
"""
__author__:liqing

创建时间:2017/3/29

文件名称:闪银web

文件用途:UI自动化
"""
from selenium import webdriver
from time import sleep
#手机配置
mobileEmulation = {'deviceName': 'Apple iPhone 5'}

#浏览器配置
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)
chromedriver = webdriver.Chrome(chrome_options=options)
chromedriver.get('http://m.wecash.net/wep/user/login.html')

#
#依据ID:输入
chromedriver.find_element_by_id('userPhone').send_keys(u'15110185703')
sleep(5)
#
#依据ID:清除
#chromedriver.find_element_by_id('userPhone').clear()
#
#依据Xpath:输入
chromedriver.find_element_by_xpath('//*[@id="password"]').send_keys(u'qazwsx')
#
#依据ClassName点击
chromedriver.find_element_by_class_name('btn-submit').click()
#打印页面title
print chromedriver.title
# # 校验:提示信息
#print chromedriver.page_source
if u'哈哈' in chromedriver.page_source:
  print u'校验内容正确~~~~'

#
# #获取属性值
attributeValue = chromedriver.find_element_by_id('userPhone').get_attribute('placeholder')
print u'获取手机号属性值为:' + attributeValue
#
# 获取文本值
textValue = chromedriver.find_element_by_id('forgotPassword').text
print u'获取忘记密码文本值为:' + textValue

# 父--子关系查找,串联查找
#chromedriver.find_element_by_xpath('//*[@id="login_int"]/div[1]/div[1]').send_keys(u'')

#
#  子--关系查找,串联查找
text = chromedriver.find_element_by_xpath('//*[@id="forgotPassword"]/..').get_attribute('class')
#print u'获取父节点属性值为:' + text
# # /parent::*/parent::
text1 =chromedriver.find_element_by_xpath('//*[@id="forgotPassword"]/parent::div').get_attribute('class')
#print u'获取父节点属性值为:' + text1

# # 弟--兄关系查找
# /preceding-sibling::
text2 = chromedriver.find_element_by_xpath('//*[@id="loginEvent"]/div[2]/span[2]/preceding-sibling::span[1]').text
#print u'获取弟定位兄节点文本值为:' + text2
#
# # 兄--弟关系查找
# # following-sibling::
text3 = chromedriver.find_element_by_xpath('//*[@id="loginEvent"]/div[2]/span[2]/following-sibling::span[1]').text
#print u'获取兄定位弟节点文本值为:' + text3

# 依据ClassName:操作:点击
chromedriver.find_element_by_class_name('btn-submit').click()